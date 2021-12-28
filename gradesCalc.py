#### PART 1 ####
# final_grade: Calculates the final grade for each student, and writes the output (while eliminating illegal
# rows from the input file) into the file in `output_path`. Returns the average of the grades.
#   input_path: Path to the file that contains the input
#   output_path: Path to the file that will contain the output


##This function check if the ID of each student is valid (check if the id has 8 numbers)
def isValidId(id):
    if (len(id) != 8):
        return False
    if (id[0] == '0'):
        return False
    for i in id:
        if (i < "0" or i > "9"):
            return False
    return True


#This fuction check if the name is valid.
def isValidName(name):
    if(name.isalpha()):
        return True
    if(name==""):
        return True
    return False

##This function check if the semester is valid
def isValidSemester(semester):
    for i in semester:
        if(i<"0" or i>"9"):
            return False
    if (int(semester) < 1):
        return False
    return True


##This function check if the average is valid
def isValidAverage(a):
    for i in a:
        if(i<"0" or i>"9"):
            return False
    if (int(a) <= 50 or int(a) > 100):
        return False
    return True

##This fucntion transform from a str line to a list without the spaces and cleaned
def returnCleanList(lines):
    final_list=[]
    for line in lines:
        final_list.append(line.split(','))
    for element in final_list:
        if(len(element)!= 4):
            continue
        element[0],element[1]=element[0].replace(" ",""),element[1].replace(" ","")
        element[2],element[3]=element[2].replace(" ",""),element[3].replace(" ","")
        element[0], element[1] = element[0].replace("\t", ""), element[1].replace("\t", "")
        element[2], element[3] = element[2].replace("\t", ""), element[3].replace("\t", "")
        if(element[3][-1:]=="\n"):
            element[3]=element[3][:-1]
    return final_list ## cette final list contient des elements de type ["535353456","iuwegfiweg","245","5465"]

##This function check if a complete line and all of the element inside are valid
def isValidCharactere(line_lst):
    if(len(line_lst)!=4):
        return False
    if (isValidId(line_lst[0])):
        if (isValidName(line_lst[1])):
            if (isValidSemester(line_lst[2])):
                if (isValidAverage(line_lst[3])):
                    return True
    return False

##this function calculate the final grade of a student
def returnFinalGrade(id,grade):
    return ((grade)+int((str(id))[6:]))//2

##this function return the actual minimum in the dictionarie
def returnMinDic(dictionaries):
    minimum=999999999
    for i in dictionaries:
        if (i<minimum):
            minimum=i
    return minimum


def final_grade(input_path: str, output_path: str) -> int:

    file_to_change = open(input_path, "r")
    my_dic = {}
    new_lines = file_to_change.readlines()
    list_of_line = returnCleanList(new_lines)
    for line in list_of_line:
        if (isValidCharactere(line)):
            line[2],line[3]=int(line[2]),int(line[3]) ## for example : ["34251255","doron",8,66]
            my_dic[int(line[0])] = line[1:]

    file_to_write = open(output_path, "w")
    sum_of_averages=0
    counter=0
    while (len(my_dic) != 0):
        min_of_the_dictionary = returnMinDic(my_dic)
        data_of_minimum = my_dic[min_of_the_dictionary]
        average = returnFinalGrade(min_of_the_dictionary, data_of_minimum[2])
        sum_of_averages+=average
        counter+=1
        final_str = str(min_of_the_dictionary) + ", " + str(data_of_minimum[2]) + ", " + str(average) + "\n"
        file_to_write.write(final_str)
        del my_dic[min_of_the_dictionary]
    file_to_change.close()
    file_to_write.close()
    if(counter !=0):
        total_average=sum_of_averages//counter
        return total_average
    return 0
    raise NotImplementedError


#### PART 2 ####
# check_strings: Checks if `s1` can be constructed from `s2`'s characters.
#   s1: The string that we want to check if it can be constructed
#   s2: The string that we want to construct s1 from

def stringToHistogram(string: str)->list:
    histogram=[0]*(26)
    for i in string:
        number=ord(i.lower())-ord('a')
        histogram[number]+=1
    return histogram

def check_strings(s1: str, s2: str) -> bool:
    # TODO: implement here
    first_histogram = stringToHistogram(s1)
    second_histogram = stringToHistogram(s2)
    for i in range(26):
        if (first_histogram[i] > second_histogram[i]):
            return False
    return True
    raise NotImplementedError
