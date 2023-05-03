movie_name = input()
student_ticket = standard_ticket = kid_ticket = total_tickets_day = 0
total_students = total_standard = total_kid = 0
ticket_type = ""
while movie_name != "Finish":
    seats_available = int(input())
    ticket_type = input()
    while ticket_type != "End":
        if ticket_type == "standard":
            standard_ticket += 1
        elif ticket_type == "kid":
            kid_ticket += 1
        elif ticket_type == "student":
            student_ticket += 1
        ticket_type = input()
        if ticket_type == "Finish" or ticket_type == "End":
            print(f"{movie_name} - {((standard_ticket + kid_ticket + student_ticket) / seats_available) * 100:.2f}% full.")
            total_tickets_day += (standard_ticket + kid_ticket + student_ticket)
            total_students += student_ticket
            total_standard += standard_ticket
            total_kid += kid_ticket
            standard_ticket = kid_ticket = student_ticket = 0

            if ticket_type == "Finish":
                print(f"Total tickets: {total_tickets_day}")
                print(f"{(total_students / total_tickets_day) * 100:.2f}% student tickets.")
                print(f"{(total_standard / total_tickets_day) * 100:.2f}% standard tickets.")
                print(f"{(total_kid / total_tickets_day) * 100:.2f}% kids tickets.")
                quit()
            else:
                movie_name = input()

quit()