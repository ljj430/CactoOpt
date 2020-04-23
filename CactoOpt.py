import pandas as pd



minCpuUtilization = 0.25
maxCpuUtilization = 0.7
minMemoryUtilization = 0.25
maxMemoryUtilization = 0.7


def OptCpuSuggestion(CpuMeasurement,assignedCpuCores):
    if CpuMeasurement > maxCpuUtilization:
        print("CPU Suggestion: +1 core")
        return assignedCpuCores + 1
    elif CpuMeasurement < minCpuUtilization:
        print("CPU Suggestion: -1 core")
        return assignedCpuCores - 1
    else:
        print("CPU Suggestion: don't change")



def OptMemorySuggestion(MemoryMeasurement,assignedMemory):
    print("Memory usage: ",MemoryMeasurement)
    if MemoryMeasurement > maxMemoryUtilization:
        print("Memory Suggestion: +1 GB")

        return assignedMemory + 1073741824
    elif MemoryMeasurement < minMemoryUtilization:


        print("Mean memory: ", MemoryMeasurement/1024/1024*assignedMemory)
        print("Memory Suggestion: ", MemoryMeasurement/1024/1024*assignedMemory*2)
        return assignedMemory - 1073741824
    else:
        print("Memory Suggestion: don't change")

def getMeanMeasurement(CpuMeasurementWithTime, memoryMeasurementWithTime, assignedCpuCores, assignedMemory):
    totalCpuMeasurement = 0
    totalMemoryMeasurement = 0
    count = 0
    for eachCpuMeasurement in CpuMeasurementWithTime:
        totalCpuMeasurement += float(eachCpuMeasurement)
    for eachMemoryMeasurement in memoryMeasurementWithTime:
        totalMemoryMeasurement += float(eachMemoryMeasurement)
        count += 1
    return totalCpuMeasurement/(count*100*assignedCpuCores),totalMemoryMeasurement/(count*assignedMemory)


#def calResponseTimeAndUsage():

if __name__ == "__main__":
    #fileName = "browsing_low_intensity_256_user_mem.csv"
    assignedCpuCores = 3
    assignedMemory = 3221225472
    #assignedMemory = 2147483648
    #fileName = "browsing_low_intensity_256_user_mem_2GB.csv"

    fileName = "browsing_low_intensity_256_user_mem_3GB.csv"
    #fileName = "browsing_med_intensity_256_user_mem_3GB.csv"
    fileName = "browsing_med_intensity_256_user_mem.csv"
    df = pd.read_csv(fileName)
    meanCpu,meanMemory = getMeanMeasurement(df.iloc[:,1],df.iloc[:,2], assignedCpuCores, assignedMemory)
    print("mean cpu:",meanCpu)
    print("mean mem:", meanMemory)

    OptCpuSuggestion(meanCpu,assignedCpuCores)
    OptMemorySuggestion(meanMemory,assignedMemory)

    ##123
    print(1)


