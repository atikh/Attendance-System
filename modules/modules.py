class Person:
    def __init__(self,firstName,lastName,nationalCode,sex,mobileNumber):
        self._firstName=firstName
        self._lastName=lastName
        self._nationalCode=nationalCode
        self._sex=sex
        self._mobileNumber=mobileNumber
    # TODO Implement Person class

class Date:
    def __init__(self,date,entrance,leaving,hourlyLeave,holiday,overTimeHours):
        #PersonID?
        self._date=date
        self._entrance=entrance
        self._leaving=leaving
        self._hourlyLeave=hourlyLeave
        self._holiday=holiday
        self._overTimeHours=overTimeHours
    # TODO Implement Date class


class OverViewMonth:
    def __init__(self, monthNo, totalDaysWorksMonth, totalEtraHoursMonth):
        # PersonID?
        # DateUD ?
        self._monthNo = monthNo
        self._totalEtraHoursMonth = totalEtraHoursMonth
        self._totalDaysWorksMonth = totalDaysWorksMonth
    # TODO Implement OverViewMonth class
