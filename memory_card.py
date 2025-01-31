from random import shuffle, randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QRadioButton, QMessageBox, QGroupBox, QButtonGroup

app = QApplication([])

main = QWidget()
main.resize(800, 400)
main.setWindowTitle('Memory Card')

question = QLabel('Какой национальности не существует?')

variants = QGroupBox('Варианты ответов')

test_result = QGroupBox('Результат теста')
yes_or_no = QLabel('Правильно/Неправильно')
answer = QLabel('Ответ будет тут!')

v_line2 = QVBoxLayout()

v_line2.addWidget(yes_or_no)
v_line2.addWidget(answer, alignment= Qt.AlignCenter)
test_result.setLayout(v_line2)

button1 = QRadioButton('Смурфы')
button2 = QRadioButton('Чулымцы')
button3 = QRadioButton('Энцы')
button4 = QRadioButton('Алеуты')

button_answer = QPushButton()
button_answer.setText('Ответить')

test_result.hide()

h_line1 = QHBoxLayout()
h_line2 = QHBoxLayout()
h_line3 = QHBoxLayout()

h_line2_1 = QHBoxLayout()
h_line2_2 = QHBoxLayout()

v_line2_1 = QVBoxLayout()

h_line2_1.addWidget(button1)
h_line2_1.addWidget(button2)
h_line2_2.addWidget(button3)
h_line2_2.addWidget(button4)

v_line2_1.addLayout(h_line2_1)
v_line2_1.addLayout(h_line2_2)

variants.setLayout(v_line2_1)

v_line1 = QVBoxLayout()

h_line1.addWidget(question, alignment= Qt.AlignCenter)
h_line2.addWidget(variants)
h_line2.addWidget(test_result)
h_line3.addStretch(1)
h_line3.addWidget(button_answer, stretch= 2)
h_line3.addStretch(1)

v_line1.addLayout(h_line1, stretch= 2)
v_line1.addLayout(h_line2, stretch= 8)
v_line1.addStretch(1)
v_line1.addLayout(h_line3, stretch= 1)
v_line1.addStretch(1)
v_line1.setSpacing(5)

main.setLayout(v_line1)

RadioGroup = QButtonGroup()
RadioGroup.addButton(button1)
RadioGroup.addButton(button2)
RadioGroup.addButton(button3)
RadioGroup.addButton(button4)

class QuestionClass():
    def __init__(self, questions, right_answer, wrong1, wrong2, wrong3):
        self.questions = questions
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

q = QuestionClass('Государственный язык Бразилии', 'Португальский', 'Испанский', 'Английский', 'Бразильский')
q1 = QuestionClass('Кто выйграл в президентских выборах в Египте в 2012 году', 'Мохаммед Мурси' , 'Эмад Абдель Гаффур', 'Аль-Саид аль-Бадави', 'Ахмед Хассан Саид')
q2 = QuestionClass('Кто побил рекорд по самому быстрому поеданию арбуза среди капибар?', 'Капибира Хэтима', 'Капибара Люффа', 'Капибара Бетти', 'Капибара Мэтью')
q3 = QuestionClass('Кто смог лучше всех скривить свое лицо на олимпиаде кривляний 2024?', 'Томми Мэттисон', 'Клэр Листер', 'Джэймс Джефферсон', 'Карен Бутлер')
q4 = QuestionClass('то изобрел розетку?', 'Харви Хабелл', 'Шэйн Такер', 'Гарри Уиллис', 'Бобби Лонг')


questions_list = []
questions_list.extend([q, q1, q2, q3, q4])

def show_result():
    variants.hide()
    test_result.show()
    button_answer.setText('Следующий вопрос')

def show_question():
    test_result.hide()
    variants.show()
    button_answer.setText('Ответить')
    RadioGroup.setExclusive(False)
    button1.setChecked(False)
    button2.setChecked(False)
    button3.setChecked(False)
    button4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [button1, button2, button3, button4]

def ask(q = QuestionClass):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.questions)
    answer.setText(q.right_answer)
    show_question()

def check_answer():
    if answers[0].isChecked():
        yes_or_no.setText('Правильно')
        show_result()
        main.score += 1
        print(f'Статистика\nВсего вопросов: {main.total}\nПравильных ответов: {main.score}')
        print(f'Рейтинг: {main.score / main.total * 100}%')
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        yes_or_no.setText('Неправильно')
        show_result()
        print(f'Рейтинг: {main.score / main.total * 100}%')

def next_question():
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    ask(q)
    main.total += 1
    print(f'Статистика\nВсего вопросов: {main.total}\nПравильных ответов: {main.score}')

def start_test():
    if button_answer.text() == 'Ответить':
        check_answer()
    else:
        next_question()

button_answer.clicked.connect(start_test)

main.score = 0
main.total = 0

next_question()
main.show()
app.exec_()
