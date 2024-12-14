import pgzrun

WIDTH = 1500
HEIGHT = 1500
TITLE = "Quiz Master"

marquee_box = Rect(0, 0, 860, 80)
question_box = Rect(0, 0, 650, 150)
timer_box = Rect(0, 0, 150, 150)
answer_box1 = Rect(0, 0, 300, 150)
answer_box2 = Rect(0, 0, 300, 150)
answer_box3 = Rect(0, 0, 300, 150)
answer_box4 = Rect(0, 0, 300, 150)
skip_box = Rect(0, 0, 150, 330)

question_file_name = "question.txt"
marquee_message = ""
score = 0
time_left = 10
is_game_over = False

answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]
questions = []
question_count = 0
question_index = 0

marquee_box.move_ip(0,0)
question_box.move_ip(20,100)
timer_box.move_ip(700,100)
answer_box1.move_ip(20,270)
answer_box2.move_ip(370,270)
answer_box3.move_ip(20,450)
answer_box4.move_ip(370,450)
skip_box.move_ip(700,270)

def draw():
    global marquee_message
    screen.clear()
    screen.fill(color = "blue")
    screen.draw.filled_rect(marquee_box, "green")
    screen.draw.filled_rect(question_box, "navy blue")
    screen.draw.filled_rect(timer_box, "dark green")
    screen.draw.filled_rect(skip_box, "red")
    for answer_box in answer_boxes:
        screen.draw.filled_rect(answer_box, "dark orange")
    marquee_message = "welcome to Quiz Master..."
    narquee_message = marquee_message+ f"Q: {question_index} of {question_count}"

    screen.draw.textbox(marquee_message, marquee_box, color = "white")
    screen.draw.textbox(str(time_left), timer_box, color = "white", shadow = (0.5, 0.5), scolor = "dim grey") 
    
    screen.draw.textbox("skip", skip_box, color = "black", angle = -90)
    screen.draw.textbox(questions[0].strip(), question_box, color = "white", 
                        shadow = (0.5, 0.5), scolor = "dim grey")
    screen.draw.textbook(
        "Skip", skip_box,
            color = "black", angle = -90
        )
    screen.draw.textbook(
        question[0].strip(), question_box,
        color = "white", shadow = (0.5,0.5),
        scolor = "dim grey"
    )

    index = 1
    for answer_box in answer_boxes:
        screen.draw.textbook(question[index].strip,(), answer_box, color = "black")
        index = index + 1


def update(): 
    move_maraquee()

def move_maraquee():
    marquee_box.x = marquee_box.x - 2
    if marquee_box.right < 0:
        marquee_box.left = WIDTH

def read_question_file():
    global question_count, questions
    q_file = open(question_file_name, "r")
    for question in q_file:
        questions.append(question)
        question_count = question_count + 1
    q_file.close()

def read_next_question():
    global question_index
    question_index = question_index + 1
    return question.pop(0).split("")

def on_mouse_down(pos):
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            if index is int(question[5]):
                correct_answer
            else:
                game_over()
        index = index + 1

    if skip_box.collidepoint(pos):
        skip_question()

def correct_answer():
    global score, question, time_left, questions
    score = score + 1
    if questions:
        question = read_next_question()
        time_left = 10
    else:
        game_over()

def game_over():
    global question, time_left, is_game_over
    message = f"Game over! \n You got {score} questions correct"
    question = [message, "-", "-", "-", "-", 5]
    time_left = 0
    is_game_over = True

def update_time_left():
    global time_left
    if time_left:
        time_left = time_left - 1
    else:
        game_over()

read_question_file()
question = read_question_file()
clock.schedule_interval(update_time_left, 1)

pgzrun.go()
