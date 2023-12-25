

class FinancePlaner():

    NUMBER_OF_MONTHS_PER_YEAR = 12

    # Investiment variables
    total_invested = 10000
    monthly_investment = 1500

    # Time
    number_of_years = 20

    # Acumulators
    average_interest = 2.5 / 100
    inflaction = 2 / 100

    # Calculations
    absolute_interest = 0
    months_calculated = 0

    is_goal_reached = False

    def calc_number_of_months(self):
        return self.NUMBER_OF_MONTHS_PER_YEAR * self.number_of_years

    def calculate_investment(self):

        for month_number in range(self.calc_number_of_months()):
            self.months_calculated += 1
            self.total_invested += self.monthly_investment

            self.total_invested += self.calculate_next_absolute_interest()

    def calculate_number_of_months_until_monthly_absolute_interest(self, goal_absolute_interest):
        absolute_interest = 0

        print(
            f"Calculating how many months it takes to reach {goal_absolute_interest} absolute interest")
        for month_number in range(self.calc_number_of_months()):
            self.months_calculated += 1
            self.total_invested += self.monthly_investment

            self.total_invested += self.calculate_next_absolute_interest()

            if absolute_interest >= goal_absolute_interest:
                self.is_goal_reached = True
                break

    def calculate_next_absolute_interest(self):
        return self.total_invested * (self.average_interest - self.inflaction)

    def print_state(self):
        GOAL_REACHED = "INDEED" if self.is_goal_reached else "NOT"
        print(
            f"Goal {GOAL_REACHED} reached after {self.months_calculated} months:")

        print(f"Total invested: {self.total_invested}")
        print(f"Monthly investment: {self.monthly_investment}")
        print(f"Number of years: {self.number_of_years}")
        print(f"Average interest: {self.average_interest}")
        print(f"Inflaction: {self.inflaction}")
        print(
            f"Absolute interest next month: {self.calculate_next_absolute_interest()}")


financePlaner = FinancePlaner()
# financePlaner.calculate_investment()


financePlaner.print_state()
# financePlaner.calculate_investment()
print("=============================================")
financePlaner.calculate_number_of_months_until_monthly_absolute_interest(
    financePlaner.monthly_investment)

financePlaner.print_state()
