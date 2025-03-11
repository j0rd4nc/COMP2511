import part2_solution

def check_report(report):
    report_ascending = report.copy()
    report_descending = report.copy()
    
    report_ascending.sort()
    report_descending.sort(reverse=True)
    
    if report_ascending != report and report_descending != report:
        return False
    
    for i in range(1, len(report)):
        if report_ascending[i] - report_ascending[i - 1] > 3 or report_ascending[i] - report_ascending[i - 1] < 1:
            return False

    return True

def dampener(report):
    for x in report:
        copy = report.copy()
        print(copy)
        copy.remove(x)
        print(copy)
        if check_report(copy) == True:
            return True
    
    return False


f = open("input.txt", "r")
reports = []
results = []

for line in f:
    report = [int(num) for num in line.split()]
    reports.append(report)
    results.append(check_report(report))

f.close()

print(results.count(True))

for i in range(len(reports)):
    if results[i] == False:
        results[i] = dampener(reports[i])

print(results.count(True))
