import pandas as pd

# Functions
def send_email(student_email, current_leaves, status):
    if status == 'warning':
        print(f'sending warning Email to {student_email}, there is only 1 more leave is left for you ')
    if status == 'alert':
        print(f'sending alert Email to {student_email} and staff, {student_email} has {current_leaves} leaves.')

#Start of program

df = pd.read_csv('Attendance.csv')
df['mailid'] = df['Student ID'].apply(lambda x : f'student_{x}@gmail.com') #adding a mail id column to the table


while True:
    print(' 1--->CI\n 2--->python\n 3--->DM')
    subject_dict = {1:'CI', 2: 'python', 3:'DM'}                #mapping each course with a number
    subject = int(input('please enter the subject (1, 2 or 3): '))
    absentee_id = input('please enter the student id of the absentees, use space to separate: ').split()
    absentee_list = [int(id) for id in absentee_id if id.isdigit() and int(id) in df['Student ID'].values]
    #at this point we have a integer list of all the absentees student ids.
    # we also checked if the entered ID actually exists in Student ID column.

    df.loc[df['Student ID'].isin(absentee_list),subject_dict[subject]] += 1
    # locating the row and column for each absentee and adding 1 to it.


    for student_id in absentee_list:
        current_leaves = df.loc[df['Student ID'] == student_id,subject_dict[subject]].values[0]
        student_email = df.loc[df['Student ID'] == student_id, 'mailid'].values[0]

        if current_leaves == 2:
            send_email(student_email,current_leaves,'warning')
        elif current_leaves >= 3:
            send_email(student_email,current_leaves,'alert')

    if int(input('another subject? 1 for Yes, 0 for No')) == 0:
         break


df.to_csv('Attendance1.csv', index= False)
print("\n✅ All updates saved to Attendance1.csv")