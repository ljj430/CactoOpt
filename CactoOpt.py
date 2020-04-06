import pandas as pd

assignedCpuCores = 3
assignedMemory = 3221225472

minCpuUtilization = 0.2
maxCpuUtilization = 0.7
minMemoryUtilization = 0.2
maxMemoryUtilization = 0.7


def OptCpuSuggestion(CpuMeasurement, assignedCpuCores):
    if CpuMeasurement > maxCpuUtilization:
        print("CPU Suggestion: +1 core")
        return assignedCpuCores + 1
    elif CpuMeasurement < minCpuUtilization:
        print("CPU Suggestion: -1 core")
        return assignedCpuCores - 1
    else:
        print("CPU Suggestion: don't change")



def OptMemorySuggestion(MemoryMeasurement, assignedMemory):
    if MemoryMeasurement > maxMemoryUtilization*assignedMemory:
        print("Memory Suggestion: +1 GB")
        return assignedMemory + 1073741824
    elif MemoryMeasurement < minMemoryUtilization*assignedMemory:
        print("Memory Suggestion: -1 GB")
        return assignedMemory - 1073741824
    else:
        print("Memory Suggestion: don't change")

def getMeanMeasurement(CpuMeasurementWithTime, memoryMeasurementWithTime):
    totalCpuMeasurement = 0
    totalMemoryMeasurement = 0
    count = 0
    for eachCpuMeasurement in CpuMeasurementWithTime:
        totalCpuMeasurement += float(eachCpuMeasurement)
    for eachMemoryMeasurement in memoryMeasurementWithTime:
        totalMemoryMeasurement += float(eachMemoryMeasurement)
        count += 1

    return totalCpuMeasurement/(count*100),totalMemoryMeasurement/count

if __name__ == "__main__":
    fileName = "browsing_low_intensity_256_user_mem.csv"
    #fileName = "browsing_medium_intensity_1_user_mem.csv"
    df = pd.read_csv(fileName)
    meanCpu,meanMemory = getMeanMeasurement(df.iloc[:,1],df.iloc[:,2])
    print(meanCpu,meanMemory)
    OptCpuSuggestion(meanCpu,assignedCpuCores)
    OptMemorySuggestion(meanMemory, assignedMemory)


