exam_start_h = int(input())
exam_start_m = int(input())
arrival_h = int(input())
arrival_m = int(input())
status = ""
exam_start_abs = (exam_start_h * 60) + exam_start_m
arrival_abs = (arrival_h * 60) + arrival_m
diff_h = diff_m = 0
if exam_start_abs == arrival_abs:
    print("On time")
    status = "Exactly On time"
elif 0 < exam_start_abs - arrival_abs <= 30:
    print("On time")
    status = "On time"
elif exam_start_abs - arrival_abs > 30:
    print("Early")
    status = "Early"
else:
    print("Late")
    status = "Late"

if status == "On time":
    print(f"{exam_start_abs - arrival_abs} minutes before the start")
elif status == "Early":
    diff_h = (exam_start_abs - arrival_abs) // 60
    if diff_h == 1:
        print(f"{exam_start_abs - arrival_abs} minutes before the start")
    elif diff_h > 1:
        print(f'{diff_h}:{} hours before the start')