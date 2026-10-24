class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # Helper function to convert "MM-DD" to day of the year
        def get_day_of_year(date_str: str) -> int:
            month = int(date_str[:2])
            day = int(date_str[3:])
            return sum(days_in_months[:month - 1]) + day
        
        # Convert all 4 dates
        alice_arrive = get_day_of_year(arriveAlice)
        alice_leave = get_day_of_year(leaveAlice)
        bob_arrive = get_day_of_year(arriveBob)
        bob_leave = get_day_of_year(leaveBob)
        
        # Find overlap range
        start = max(alice_arrive, bob_arrive)
        end = min(alice_leave, bob_leave)
        
        # Calculate total overlapping days
        return max(0, end - start + 1)