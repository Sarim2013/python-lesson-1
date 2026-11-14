import pgzrun, random
from pygame import Rect
TITLE = "Quiz Master"
WIDTH = 800
HEIGHT = 550
marque_box = Rect(0,0, 800,60) #(x,y, w,h)
question_box = Rect(20,80, 550,150)
timer_box = Rect(630,80, 150,150)
skip_box = Rect(630,240, 150,300)
ans_box_1 = Rect(20,250, 245,120)
ans_box_2 = Rect(320,250, 245,120)
ans_box_3 = Rect(20,400, 245,120)
ans_box_4 = Rect(320,400, 245,120)

answer_boxes = [ans_box_1, ans_box_2, ans_box_3, ans_box_4]
#game variables
score = 0
time_left = 5
marque_message = ""
is_game_over = False

question_file_name="quizmaster\\questions.txt"
questions=[]
question_count=0 #total number of questions
question_index=0 #current question number


def draw():
    screen.fill("black")
    screen.draw.filled_rect(marque_box, "blue")
    screen.draw.filled_rect(question_box, "red")
    screen.draw.filled_rect(timer_box, "red")
    screen.draw.filled_rect(skip_box, "green")
    #to draw answer boxes
    for ans_box in answer_boxes:
        screen.draw.filled_rect(ans_box, "orange")

    #marque box message
    marque_message = "Welcome To Quiz Master"
    marque_message += f"Q: {question_index} out of {question_count}"
    # to display marque text
    screen.draw.text(marque_message, marque_box, color = "white")










pgzrun.go()