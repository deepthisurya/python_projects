#Find out the simple interest

# We know Simple interest S.I = (p.t.r)/100
# p - Principal amount
# t - time period
# r - rate of interest

#Collect information from the user
def get_data_SI():
    principal_amount = int(input("Provide the principal amount - "))
    time_period = int(input("What is the total period of loan - "))
    rate_of_interest = int(input("What is the rate of interest - "))
    return principal_amount,time_period,rate_of_interest

#Compute the simple interest based on user data
def simple_interest():
    principal_amount,time_period,rate_of_interest = get_data_SI()
    return (principal_amount*time_period*rate_of_interest)/100

#Main function printing the computed data - ok

if __name__ == '__main__':
    print("The Simple Interest for given information - ",simple_interest())