#-------------------------------------------------------------------------------
# Name:        Grades Version 3 [grades_files]
# Purpose:      Calculates grades and outputs to a File
#
# Author:      Joshua Cleary
#
# Created:     05/01/2023
#-------------------------------------------------------------------------------
import datetime
stu = []
student_file = "students.csv"
out_file = "stu_report.txt"

def main():
    read_data_file()
    calculate_grades()
    create_report_file()

def read_data_file():
    datafile = open(student_file, "r")
    lines = datafile.readlines()
    for i in lines:
        stu.append(i.split(",")) # split data by commas, add to list
    datafile.close()

def calculate_grades():
    global average, totA, totB, totC, totD, totF
    totA = totB = totC = totD = totF = 0
    gradestotal = 0

    for i in range(len(stu)):
        hw = int(stu[i][2]) # last name is pos 0, first is 1, howework is 2
        midex = int(stu[i][3])
        stu[i][4] = stu[i][4][:-1] #Remove the \n from the final exam string
        finex = int(stu[i][4]) # Final exam in pos 4
        sum_grades = hw + midex + finex
        finalgr = sum_grades / 3
        gradestotal += finalgr # adds grades to total
        stu[i].append(finalgr)

        if finalgr >= 90:
            lettergrade = 'A'
            totA += 1
        elif finalgr >= 80:
            lettergrade = 'B'
            totB += 1
        elif finalgr >= 70:
            lettergrade = 'C'
            totC += 1
        elif finalgr >= 0:
            lettergrade = 'D'
            totD += 1
        else:
            lettergrade = 'F'
            totF += 1
        stu[i].append(lettergrade)
    average = gradestotal / len(stu)

def create_report_file():
    line = "\n*************************************************"
    repfile = open(out_file,"w")
    repfile.write("\n****************** CSC 230 Grade Report ******************")
    repfile.write("\nReport Date/Time        : " + str(datetime.datetime.now()))
    repfile.write("\nTotal number of students: " + str(len(stu)))
    repfile.write("\nAverage student grade   : " + format(average, '5,.2f'))
    repfile.write("\nTotal number of A grades: " + str(totA))
    repfile.write("\nTotal number of B grades: " + str(totB))
    repfile.write("\nTotal number of C grades: " + str(totC))
    repfile.write("\nTotal number of D grades: " + str(totD))
    repfile.write("\nTotal number of F grades: " + str(totF))
    repfile.write(line)
    repfile.write("\nNAME                     HW\tMID\tFIN\tFINAL GRADE")
    repfile.write(line)
    for i  in range(len(stu)):
        sname = '{0:<18}'.format(stu[i][0]+', '+ stu[i][1])
        hw = str(stu[i][2])
        midex = str(stu[i][3])
        finex = str(stu[i][4])
        fingrade = format(stu[i][5], '6,.2f')
        repfile.write("\n"+ sname + "\t" + hw + "\t" + midex + "\t" + finex + "\t" + fingrade + " " + stu[i][6])
    repfile.write(line)
    repfile.close()
    print("Open this file to view the Grades Report: " + out_file)

main()
