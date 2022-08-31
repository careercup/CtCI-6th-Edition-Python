from queue import Queue
from datetime import datetime

EMPLOYEE = "employee"
RESPONDENT = "respondent"
MANAGER = "manager"
DIRECTOR = "director"


class Person:
    def __init__(self, name: str):
        self.name = name.title()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Employee(Person):
    def __init__(self, call_center, **kwargs):
        super().__init__(**kwargs)
        self.grade = EMPLOYEE
        self.superior = None
        self.current_call = None
        self.call_center = call_center

    def is_free(self):
        return self.current_call is None

    def take_call(self, call):
        if not self.is_free():
            raise ValueError("Employee is busy and can not take the call right now.")
        self.current_call = call
        self.current_call.employees.append(self)
        print(f"Hello {call.person}, my name is {self}. How can I help you?")

    def escalate_call(self):
        if self.current_call is None:
            raise ValueError("No call to escalate.")
        self.call_center.dispatch_call(self.current_call, send_to=self.superior)
        self.take_next_call()

    def end_call(self):
        if self.current_call is None:
            raise ValueError("No call to end.")
        self.current_call.end_time = datetime.now()
        print(f"{self} here. Call ended with {self.current_call.person}.")
        self.call_center.archive_call(self.current_call)
        self.current_call = None
        self.take_next_call()

    def take_next_call(self):
        queue_ = self.call_center.queues[self.grade]
        if not queue_.empty():
            next_call = queue_.get()
            self.take_call(next_call)
        else:
            self.current_call = None


class Respondent(Employee):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.superior = MANAGER
        self.grade = RESPONDENT


class Manager(Employee):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.superior = DIRECTOR
        self.grade = MANAGER


class Director(Employee):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.superior = None
        self.grade = DIRECTOR

    def escalate_call(self):
        pass

    def take_next_call(self):
        super().take_next_call()
        manager_queue = self.call_center.queues[MANAGER]
        if self.is_free() and not manager_queue.empty():
            next_call = manager_queue.get()
            self.take_call(next_call)


class Call:
    def __init__(self, person: Person):
        self.person = person
        self.start_time = datetime.now()
        self.employees = []
        self.end_time = None

    def __repr__(self):
        resp = f"Call from {self.person}, started at {self.start_time}. Employees in charge: {'->'.join(str(employee) for employee in self.employees)}."
        if self.end_time is not None:
            resp += f" Ended at {self.end_time}."
        return resp

    def __str__(self):
        resp = f"Call from {self.person}, started at {self.start_time}. Employees in charge: {'->'.join(str(employee) for employee in self.employees)}."
        if self.end_time is not None:
            resp += f" Ended at {self.end_time}."
        return resp


class CallCenter:
    def __init__(self):
        self.employees = {RESPONDENT: [], MANAGER: [], DIRECTOR: []}
        self.queues = {RESPONDENT: Queue(), MANAGER: Queue(), DIRECTOR: Queue()}
        self.archives = []

    def dispatch_call(self, call: Call, send_to: str = RESPONDENT):
        for employee in self.employees[send_to]:
            if employee.is_free():
                print(f"You will soon talk to our {send_to} {employee}.")
                employee.take_call(call)
                return
        if send_to == MANAGER:
            # if no manager is free, we check if a director is
            for employee in self.employees[DIRECTOR]:
                if employee.is_free():
                    print(f"You will soon talk to our {DIRECTOR} {employee}.")
                    employee.take_call(call)
                    return
        self.queues[send_to].put(call)
        return print(
            f"None of our {send_to}s are available right now, please wait a moment."
        )

    def archive_call(self, call: Call):
        self.archives.append(call)

    def add_employees(self, employees_list: list):
        for employee in employees_list:
            self.employees[employee.grade].append(employee)

    def print_archives(self):
        print("Calls archives:")
        for call in self.archives:
            print(call)


if __name__ == "__main__":
    center = CallCenter()
    alex = Director(name="alex", call_center=center)
    john = Manager(name="john", call_center=center)
    andre = Respondent(name="andre", call_center=center)
    hugo = Respondent(name="hugo", call_center=center)
    center.add_employees([alex, john, andre, hugo])

    for name in ["samantha", "robert", "edmond"]:
        call = Call(person=Person(name=name))
        center.dispatch_call(call)

    andre.end_call()
    hugo.escalate_call()
    john.escalate_call()

    call = Call(person=Person(name="gerard"))
    center.dispatch_call(call)

    hugo.escalate_call()
    john.escalate_call()
    alex.end_call()
    alex.end_call()

    center.print_archives()
