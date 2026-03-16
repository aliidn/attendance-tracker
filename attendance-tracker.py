import pandas as pd

df = pd.read_csv('Attendance.csv')
df['mailid'] = df['Student ID'].apply(lambda x : f'student_{x}@gmail.com') #adding a mail id column to the table

print('1--->CI\n2--->python\n3--->DM')
subject_dict = {1:'CI', 2: 'python', 3:'DM'} #mapping each course with a number
subject = int(input('please enter the subject: '))
absentee_id = input('please enter the student id of the absentees: ').split(' ')
absentee_list = [int(id) for id in absentee_id] #at this point we have a integer list of all the absentees ids

df.loc[df['Student ID'].isin(absentee_list),subject_dict[subject]] += 1 #locationg the row and column for each absentee.

df.to_csv('Attendance1.csv', index= False)