import sqlite3
import sys
import shutil
import os
import random
import pymorphy3

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLineEdit, QFileDialog, QAbstractItemView

from data.main_menu import MainMenuUi
from data.entrance import EntranceUi
from data.registration import RegistrationUi
from data.login import LoginUi
from data.student_choice import StudentChoiceUi
from data.profile import ProfileUi
from data.profile_edit import ProfileEditUi
from data.test_type import TestTypeUi
from data.comparison import ComparisonUi
from data.result import ResultUi
from data.definition import DefinitionUi
from data.answers import AnswersUi
from data.test import TestUi
from data.picture_comparison import PictureComparisonUi
from data.my_tests import MyTestsUi
from data.term_create import TermCreateUi
from data.create_test_student import CreateTestStudentUi
from data.finish import FinishUi
from data.test_editor import TestEditorUi
from data.picture_comparison_editor import PictureComparisonEditorUi

morph = pymorphy3.MorphAnalyzer()


class Entrance(QWidget, EntranceUi):
    def __init__(self):
        super(Entrance, self).__init__()
        self.setupUi(self)
        self.click_btn()

    def click_btn(self):
        self.pushButton.clicked.connect(self.open_login)
        self.pushButton_2.clicked.connect(self.open_registration)

    def open_login(self):
        self.login = Login()
        self.close()
        self.login.show()

    def open_registration(self):
        self.registration = Registration()
        self.close()
        self.registration.show()


class Login(QWidget, LoginUi):
    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)
        self.click_btn()

    def click_btn(self):
        self.backBtn.clicked.connect(self.back)
        self.showPassBtn.clicked.connect(self.show_hide_password)
        self.entranceBtn.clicked.connect(self.login)

    def back(self):
        self.entrance = Entrance()
        self.close()
        self.entrance.show()

    def show_hide_password(self):
        if self.showPassBtn.isChecked():
            self.passwordEdit.setEchoMode(QLineEdit.Normal)
        else:
            self.passwordEdit.setEchoMode(QLineEdit.Password)

    def login(self):
        nickname = None
        with sqlite3.connect('data/trainer_db') as con:
            if self.loginEdit.text() == '' or self.passwordEdit.text() == '':
                self.messageLabel.setText('Введите логин и пароль!')
            else:
                check = con.cursor().execute("""SELECT password FROM user
                                                    WHERE nickname = ?""", (self.loginEdit.text(),)).fetchone()
                if check is not None:
                    if self.passwordEdit.text() == check[0]:
                        nickname = self.loginEdit.text()
                        self.main = Main(nickname)
                        self.close()
                        self.main.show()
                if not nickname:
                    self.messageLabel.setText('Неверный логин или пароль')


class Registration(QWidget, RegistrationUi):
    def __init__(self):
        super(Registration, self).__init__()
        self.setupUi(self)
        self.click_btn()

    def click_btn(self):
        self.backBtn.clicked.connect(self.back)
        self.showPassBtn.clicked.connect(self.show_hide_password)
        self.createBtn.clicked.connect(self.create_account)

    def back(self):
        self.entrance = Entrance()
        self.close()
        self.entrance.show()

    def show_hide_password(self):
        if self.showPassBtn.isChecked():
            self.passwordEdit.setEchoMode(QLineEdit.Normal)
            self.passwordEdit2.setEchoMode(QLineEdit.Normal)
        else:
            self.passwordEdit.setEchoMode(QLineEdit.Password)
            self.passwordEdit2.setEchoMode(QLineEdit.Password)

    def create_account(self):
        if self.loginEdit.text() == '' or self.passwordEdit.text() == '':
            self.messageLabel.setText('Введите логин и пароль!')
        else:
            with sqlite3.connect('data/trainer_db') as con:
                check = con.cursor().execute("""SELECT id FROM user
                 WHERE nickname = ?""", (self.loginEdit.text(),)).fetchone()
                if check is not None:
                    self.messageLabel.setText('Имя пользователя уже занято.')
                elif self.passwordEdit.text() != self.passwordEdit2.text():
                    self.messageLabel.setText('Пароли не совпадают.')
                else:
                    nickname = self.loginEdit.text()
                    password = self.passwordEdit.text()
                    if self.studentBtn.isChecked():
                        status = 'Ученик'
                    else:
                        status = 'Учитель'
                    con.cursor().execute("""INSERT INTO user
                                        (nickname, password, status)
                                        VALUES (?, ?, ?);""", (nickname, password, status))
                    con.commit()
                    self.main = Main(nickname)
                    self.close()
                    self.main.show()


class Main(QMainWindow, MainMenuUi):
    def __init__(self, nickname):
        super(Main, self).__init__()
        self.nickname = nickname
        self.setupUi(self)
        self.accountBtn.setText(self.nickname)
        self.accountBtn.adjustSize()
        with sqlite3.connect('data/trainer_db') as con:
            avatar = con.cursor().execute("""SELECT avatar FROM user
                 WHERE nickname = ?""", (self.nickname,)).fetchone()[0]
            if avatar is not None:
                if os.path.isfile(avatar):
                    self.avatarLabel.setPixmap(QtGui.QPixmap(avatar))
        self.click_btn()

    def click_btn(self):
        self.physicsBtn.clicked.connect(self.open_physics)
        self.biologyBtn.clicked.connect(self.open_biology)
        self.chemistryBtn.clicked.connect(self.open_chemistry)
        self.geographyBtn.clicked.connect(self.open_geography)
        self.accountBtn.clicked.connect(self.open_profile)

    def open_physics(self):
        self.choice = StudentChoice(self.nickname, 'physics')
        self.close()
        self.choice.show()

    def open_biology(self):
        self.choice = StudentChoice(self.nickname, 'biology')
        self.close()
        self.choice.show()

    def open_chemistry(self):
        self.choice = StudentChoice(self.nickname, 'chemistry')
        self.close()
        self.choice.show()

    def open_geography(self):
        self.choice = StudentChoice(self.nickname, 'geography')
        self.close()
        self.choice.show()

    def open_profile(self):
        self.profile = Profile(self.nickname)
        self.close()
        self.profile.show()


class StudentChoice(QWidget, StudentChoiceUi):
    def __init__(self, nickname, subject):
        super(StudentChoice, self).__init__()
        self.nickname = nickname
        self.subject = subject
        self.setupUi(self)
        self.click_btn()

    def click_btn(self):
        self.backBtn.clicked.connect(self.back)
        self.exampleBtn.clicked.connect(self.open_example)
        self.myTestsBtn.clicked.connect(self.open_my_tests)

    def back(self):
        self.main = Main(self.nickname)
        self.close()
        self.main.show()

    def open_example(self):
        self.test_type = TestType(self.nickname, self.subject)
        self.close()
        self.test_type.show()

    def open_my_tests(self):
        self.my_tests = MyTests(self.nickname, self.subject)
        self.close()
        self.my_tests.show()

    def open_teachers_tests(self):
        pass


class MyTests(QWidget, MyTestsUi):
    def __init__(self, nickname, subject):
        super(MyTests, self).__init__()
        self.nickname = nickname
        self.subject = subject
        self.setupUi(self)
        self.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.fill()
        self.click_btn()

    def fill(self):
        self.model = QtCore.QStringListModel(self)
        with sqlite3.connect('data/trainer_db') as con:
            tests = con.cursor().execute('''SELECT test_name FROM student_tests WHERE 
            author = ? AND subject = ?''', (self.nickname, self.subject)).fetchall()
            if len(tests) > 0:
                a = [i[0] for i in tests]
                self.model.setStringList(a)
                self.listView.setModel(self.model)
            else:
                self.messageLabel.setText('Здесь будут ваши тесты')

    def click_btn(self):
        self.backBtn.clicked.connect(self.back)
        self.createBtn.clicked.connect(self.create_test)
        self.listView.doubleClicked.connect(self.open_test)

    def back(self):
        self.choice = StudentChoice(self.nickname, self.subject)
        self.close()
        self.choice.show()

    def create_test(self):
        self.create_test_student = CreateTestStudent(self.nickname, self.subject)
        self.close()
        self.create_test_student.show()

    def open_test(self):
        with sqlite3.connect('data/trainer_db') as con:
            data = con.cursor().execute('''SELECT test_type, reversed FROM student_tests WHERE 
                test_name = ?''', (self.listView.currentIndex().data(),)).fetchone()
            if len(data) > 1:
                if data[1] == 0:
                    reverse = False
                else:
                    reverse = True
            if data[0] == 'Сопоставление термин-определение':
                self.comparison = Comparison(self.nickname, self.subject, self.listView.currentIndex().data(),
                                             reverse=reverse)
                self.close()
                self.comparison.show()
            elif data[0] == 'Написание определения':
                self.definition = Definition(self.nickname, self.subject, self.listView.currentIndex().data(),
                                             reverse=reverse)
                self.close()
                self.definition.show()
            elif data[0] == 'Тест с вариантами ответа':
                self.definition = Test(self.nickname, self.subject, self.listView.currentIndex().data())
                self.close()
                self.definition.show()
            elif data[0] == 'Сопоставление с картинками':
                self.pic_comp = PictureComparison(self.nickname, self.subject, self.listView.currentIndex().data())
                self.close()
                self.pic_comp.show()


class CreateTestStudent(QWidget, CreateTestStudentUi):
    def __init__(self, nickname, subject):
        super(CreateTestStudent, self).__init__()
        self.nickname = nickname
        self.subject = subject
        self.setupUi(self)
        self.click_btn()

    def click_btn(self):
        self.backBtn.clicked.connect(self.back)
        self.createBtn.clicked.connect(self.create_test)

    def back(self):
        self.my_tests = MyTests(self.nickname, self.subject)
        self.close()
        self.my_tests.show()

    def create_test(self):
        if len(self.lineEdit.text()) > 0:
            for i in self.buttonGroup.buttons():
                if i.isChecked():
                    self.test_type = i.text()
            with sqlite3.connect('data/trainer_db') as con:
                check = con.cursor().execute(f"""SELECT id FROM student_tests 
                WHERE test_name like '{self.lineEdit.text()}%' AND author = ?""", (self.nickname,)).fetchall()
                if len(check) > 0:
                    self.test_name = f'{self.lineEdit.text()}_{len(check) + 1}'
                    file = open(f'data/{self.subject}/{self.lineEdit.text()}_{len(check) + 1}.txt', 'w+')
                    file.close()
                else:
                    self.test_name = self.lineEdit.text()
                    file = open(f'data/{self.subject}/{self.lineEdit.text()}.txt', 'w+')
                    file.close()
                if self.test_type == 'Сопоставление термин-определение' or self.test_type == 'Написание определения':
                    self.term_create = TermCreate(self.nickname, self.subject, self.test_name, self.test_type)
                    self.close()
                    self.term_create.show()
                elif self.test_type == 'Тест с вариантами ответа':
                    self.test_editor = TestEditor(self.nickname, self.subject, self.test_name)
                    self.close()
                    self.test_editor.show()
                else:
                    self.pic_comp_editor = PictureComparisonEditor(self.nickname, self.subject, self.test_name)
                    self.close()
                    self.pic_comp_editor.show()
        else:
            self.messageLabel.setText('Введите название теста')


class TermCreate(QWidget, TermCreateUi):
    def __init__(self, nickname, subject, test_name, test_type):
        super(TermCreate, self).__init__()
        self.nickname = nickname
        self.subject = subject
        self.test_name = test_name
        self.test_type = test_type
        self.setupUi(self)
        self.click_btn()

    def click_btn(self):
        self.backBtn.clicked.connect(self.back)
        self.pushButton_2.clicked.connect(self.add_term)
        self.pushButton.clicked.connect(self.end_creating)

    def back(self):
        self.create_test_student = CreateTestStudent(self.nickname, self.subject)
        os.remove(f'data/{self.subject}/{self.test_name}.txt')
        self.close()
        self.create_test_student.show()

    def add_term(self):
        if len(self.textEdit_1.toPlainText()) > 0 and len(self.textEdit_2.toPlainText()) > 0:
            with open(f'data/{self.subject}/{self.test_name}.txt', 'a+', encoding='utf-8') as f:
                f.write(
                    f'''{' '.join(self.textEdit_1.toPlainText().split('\n'))} - {' '.join(self.textEdit_2.toPlainText().split('\n'))}\n''')
                self.messageLabel.setText('')
                self.textEdit_1.setText('')
                self.textEdit_2.setText('')
        else:
            self.messageLabel.setText('Поля не заполнены!')

    def end_creating(self):
        with open(f'data/{self.subject}/{self.test_name}.txt', 'r', encoding='utf-8') as f:
            if len(f.readlines()) >= 4:
                self.finish = Finish(self.nickname, self.test_name, self.test_type, self.subject)
                self.close()
                self.finish.show()
            else:
                self.messageLabel.setText('Введите минимум 4 определения!')


class Finish(QWidget, FinishUi):
    def __init__(self, nickname, test_name, test_type, subject):
        super(Finish, self).__init__()
        self.nickname = nickname
        self.test_name = test_name
        self.test_type = test_type
        self.subject = subject
        self.setupUi(self)
        self.click_btn()

    def click_btn(self):
        self.pushButton.clicked.connect(self.finish)

    def finish(self):
        for i in self.buttonGroup.buttons():
            if i.isChecked():
                if i.text() == 'термин -> определение':
                    self.reverse = 0
                else:
                    self.reverse = 1
        with sqlite3.connect('data/trainer_db') as con:
            con.cursor().execute("""INSERT INTO student_tests
                                (author, test_name, test_type, subject, reversed)
                                VALUES (?, ?, ?, ?, ?);""",
                                 (self.nickname, self.test_name, self.test_type, self.subject, self.reverse))
        self.my_tests = MyTests(self.nickname, self.subject)
        self.close()
        self.my_tests.show()


class TestEditor(QWidget, TestEditorUi):
    def __init__(self, nickname, subject, test_name):
        super(TestEditor, self).__init__()
        self.nickname = nickname
        self.subject = subject
        self.test_name = test_name
        self.setupUi(self)
        self.click_btn()

    def click_btn(self):
        self.backBtn.clicked.connect(self.back)
        self.pushButton_2.clicked.connect(self.add_question)
        self.pushButton.clicked.connect(self.end_creating)

    def back(self):
        self.create_test_student = CreateTestStudent(self.nickname, self.subject)
        os.remove(f'data/{self.subject}/{self.test_name}.txt')
        self.close()
        self.create_test_student.show()

    def add_question(self):
        if len(self.questionText.toPlainText()) > 0 and len(self.textEdit_1.toPlainText()) > 0 and len(
                self.textEdit_2.toPlainText()) > 0 and len(self.textEdit_3.toPlainText()) > 0 and len(
                self.textEdit_4.toPlainText()) > 0:
            if any(map(lambda x: x.isChecked(), self.buttonGroup.buttons())):
                with open(f'data/{self.subject}/{self.test_name}.txt', 'a+', encoding='utf-8') as f:
                    texts = [' '.join(self.textEdit_1.toPlainText().split('\n')),
                             ' '.join(self.textEdit_2.toPlainText().split('\n')),
                             ' '.join(self.textEdit_3.toPlainText().split('\n')),
                             ' '.join(self.textEdit_4.toPlainText().split('\n'))]
                    for i in self.buttonGroup.buttons():
                        if i.isChecked():
                            ans = texts[int(i.objectName()[-1]) - 1]
                            texts.pop(int(i.objectName()[-1]) - 1)
                    f.write(
                        f'''{' '.join(self.questionText.toPlainText().split('\n'))} - {ans} | {texts[0]} | {texts[1]} | {texts[2]}\n''')
                    self.messageLabel.setText('')
                    self.textEdit_1.setText('')
                    self.textEdit_2.setText('')
                    self.textEdit_3.setText('')
                    self.textEdit_4.setText('')
                    self.questionText.setText('')
            else:
                self.messageLabel.setText('Выберите верный вариант ответа!')
        else:
            self.messageLabel.setText('Заполните все поля!')

    def end_creating(self):
        with open(f'data/{self.subject}/{self.test_name}.txt', 'r', encoding='utf-8') as f:
            if len(f.readlines()) > 0:
                with sqlite3.connect('data/trainer_db') as con:
                    con.cursor().execute("""INSERT INTO student_tests
                                        (author, test_name, test_type, subject)
                                        VALUES (?, ?, ?, ?);""",
                                         (self.nickname, self.test_name, 'Тест с вариантами ответа', self.subject))
                self.my_tests = MyTests(self.nickname, self.subject)
                self.close()
                self.my_tests.show()
            else:
                self.messageLabel.setText('Добавьте хотя бы 1 вопрос!')


class PictureComparisonEditor(QWidget, PictureComparisonEditorUi):
    def __init__(self, nickname, subject, test_name):
        super(PictureComparisonEditor, self).__init__()
        self.nickname = nickname
        self.subject = subject
        self.test_name = test_name
        self.setupUi(self)
        self.click_btn()

    def click_btn(self):
        self.backBtn.clicked.connect(self.back)
        self.pushButton_2.clicked.connect(self.add_exercise)
        self.pushButton.clicked.connect(self.end_creating)
        self.addPictureBtn.clicked.connect(self.add_picture)

    def back(self):
        self.create_test_student = CreateTestStudent(self.nickname, self.subject)
        os.remove(f'data/{self.subject}/{self.test_name}.txt')
        self.close()
        self.create_test_student.show()

    def add_picture(self):
        try:
            pic = QFileDialog.getOpenFileName(
                self, 'Выбрать картинку', '',
                'Картинка (*.jpg);;Картинка (*.png)')[0]
            self.pic = f'data/{self.subject}/pictures/{pic.split("/")[-1]}'
            shutil.copy(pic, self.pic)
            pixmap = QtGui.QPixmap(self.pic)
            w, h = pixmap.size().width(), pixmap.size().height()
            self.pictureLabel.resize(int(160 / h * w), 160)
            self.addPictureBtn.resize(int(160 / h * w), 160)
            self.pictureLabel.setPixmap(pixmap)
        except FileNotFoundError:
            self.messageLabel.setText('Картинка не найдена')

    def add_exercise(self):
        if len(self.textEdit_1.toPlainText()) > 0 and self.pictureLabel.pixmap():
            with open(f'data/{self.subject}/{self.test_name}.txt', 'a+', encoding='utf-8') as f:
                f.write(
                    f'''{' '.join(self.textEdit_1.toPlainText().split('\n'))} - {self.pic}\n''')
                self.messageLabel.setText('')
                self.textEdit_1.setText('')
                self.pictureLabel.clear()
        else:
            self.messageLabel.setText('Заполните поля!')

    def end_creating(self):
        with open(f'data/{self.subject}/{self.test_name}.txt', 'r', encoding='utf-8') as f:
            if len(f.readlines()) >= 4:
                with sqlite3.connect('data/trainer_db') as con:
                    con.cursor().execute("""INSERT INTO student_tests
                                        (author, test_name, test_type, subject)
                                        VALUES (?, ?, ?, ?);""",
                                         (self.nickname, self.test_name, 'Сопоставление с картинками', self.subject))
                self.my_tests = MyTests(self.nickname, self.subject)
                self.close()
                self.my_tests.show()
            else:
                self.messageLabel.setText('Добавьте минимум 4 картинки!')


class TestType(QWidget, TestTypeUi):
    def __init__(self, nickname, subject):
        super(TestType, self).__init__()
        self.nickname = nickname
        self.subject = subject
        self.setupUi(self)
        self.click_btn()

    def click_btn(self):
        self.backBtn.clicked.connect(self.back)
        self.pushButton.clicked.connect(self.open_comparison)
        self.pushButton_2.clicked.connect(self.open_definition)
        self.pushButton_3.clicked.connect(self.open_test)
        self.pushButton_4.clicked.connect(self.open_pictures_comparison)

    def back(self):
        self.student_choice = StudentChoice(self.nickname, self.subject)
        self.close()
        self.student_choice.show()

    def open_comparison(self):
        self.comparison = Comparison(self.nickname, self.subject, f'comparison_example_{self.subject}', True)
        self.close()
        self.comparison.show()

    def open_definition(self):
        self.definition = Definition(self.nickname, self.subject, f'comparison_example_{self.subject}', True)
        self.close()
        self.definition.show()

    def open_test(self):
        self.test = Test(self.nickname, self.subject, f'test_example_{self.subject}', True)
        self.close()
        self.test.show()

    def open_pictures_comparison(self):
        self.pic_comp = PictureComparison(self.nickname, self.subject, f'pic_comp_example_{self.subject}', True)
        self.close()
        self.pic_comp.show()


class Profile(QWidget, ProfileUi):
    def __init__(self, nickname):
        super(Profile, self).__init__()
        self.nickname = nickname
        self.setupUi(self)
        with sqlite3.connect('data/trainer_db') as con:
            data = con.cursor().execute("""SELECT avatar, status FROM user
                 WHERE nickname = ?""", (self.nickname,)).fetchone()
            if data[0] is not None:
                if os.path.isfile(data[0]):
                    self.avatarLabel.setPixmap(QtGui.QPixmap(data[0]))
            self.statusLabel.setText(data[1])
        self.nameLabel.setText(self.nickname)
        self.click_btn()

    def click_btn(self):
        self.backBtn.clicked.connect(self.back)
        self.editAccBtn.clicked.connect(self.open_edit)
        self.changeAccBtn.clicked.connect(self.change_account)

    def back(self):
        self.main = Main(self.nickname)
        self.close()
        self.main.show()

    def open_edit(self):
        self.edit = ProfileEdit(self.nickname)
        self.close()
        self.edit.show()

    def change_account(self):
        self.entrance = Entrance()
        self.close()
        self.entrance.show()


class ProfileEdit(QWidget, ProfileEditUi):
    def __init__(self, nickname):
        super(ProfileEdit, self).__init__()
        self.avatar = None
        self.nickname = nickname
        self.setupUi(self)
        self.nameEdit.setText(self.nickname)
        with sqlite3.connect('data/trainer_db') as con:
            data = con.cursor().execute("""SELECT password, avatar FROM user
             WHERE nickname = ?""", (self.nickname,)).fetchone()
            password = data[0]
            if data[1]:
                self.avatar = data[1]
                if os.path.isfile(self.avatar):
                    self.avatarLabel.setPixmap(QtGui.QPixmap(self.avatar))
        self.passwordEdit.setText(password)
        self.click_btn()

    def click_btn(self):
        self.backBtn.clicked.connect(self.back)
        self.showPassBtn.clicked.connect(self.show_hide_password)
        self.acceptBtn.clicked.connect(self.accept_changes)
        self.avatarBtn.clicked.connect(self.change_avatar)

    def back(self):
        self.profile = Profile(self.nickname)
        self.close()
        self.profile.show()

    def show_hide_password(self):
        if self.showPassBtn.isChecked():
            self.passwordEdit.setEchoMode(QLineEdit.Normal)
        else:
            self.passwordEdit.setEchoMode(QLineEdit.Password)

    def change_avatar(self):
        try:
            avatar = QFileDialog.getOpenFileName(
                self, 'Выбрать картинку', '',
                'Картинка (*.jpg);;Картинка (*.png)')[0]
            self.avatar = f'data/avatars/{avatar.split("/")[-1]}'
            shutil.copy(avatar, self.avatar)
            self.avatarLabel.setPixmap(QtGui.QPixmap(self.avatar))
        except FileNotFoundError:
            self.messageLabel.setText('Картинка не найдена')

    def accept_changes(self):
        if self.nameEdit.text() == '' or self.passwordEdit.text() == '':
            self.messageLabel.setText('Введите логин и пароль!')
        else:
            with sqlite3.connect('data/trainer_db') as con:
                if self.nameEdit.text() == self.nickname:
                    check = None
                else:
                    check = con.cursor().execute("""SELECT id FROM user
                     WHERE nickname = ?""", (self.nameEdit.text(),)).fetchone()
                if check is not None:
                    self.messageLabel.setText('Имя пользователя уже занято.')
                else:
                    nickname = self.nameEdit.text()
                    password = self.passwordEdit.text()
                    con.cursor().execute("""UPDATE user SET nickname = ?, password = ?, avatar = ? 
                    WHERE nickname = ?""", (nickname, password, self.avatar, self.nickname))
                    con.commit()
                    self.nickname = nickname
                    self.back()


class Comparison(QWidget, ComparisonUi):
    def __init__(self, nickname, subject, name, example=False, reverse=False):
        super(Comparison, self).__init__()
        self.nickname = nickname
        self.subject = subject
        self.example = example
        self.name = name
        self.reverse = reverse
        self.ans_field = None
        self.right = 0
        self.setupUi(self)
        with open(f'data/{self.subject}/{self.name}.txt', encoding='utf-8') as f:
            self.f = list(map(lambda x: x.rstrip().split(' - '), f.readlines()))
            self.f1 = self.f.copy()
        self.fill_fields()
        self.click_btn()

    def click_btn(self):
        self.backBtn.clicked.connect(self.back)
        self.continueBtn.clicked.connect(self.check)

    def back(self):
        self.test_type = TestType(self.nickname, self.subject)
        self.close()
        self.test_type.show()

    def fill_fields(self):
        f2 = self.f.copy()
        fields = [self.textEdit_1, self.textEdit_2, self.textEdit_3, self.textEdit_4]
        random.shuffle(fields)
        if not self.reverse:
            a = ex, ans = random.choice(self.f1)
        else:
            a = ans, ex = random.choice(self.f1)
        self.f1.remove(a)
        f2.remove(a)
        self.exerciseText.setText(ex)
        self.ans_field = random.choice(fields)
        self.ans_field.setText(ans)
        fields.remove(self.ans_field)
        random.shuffle(f2)
        if not self.reverse:
            for i in range(3):
                fields[0].setText(f2[i][1])
                fields.pop(0)
        else:
            for i in range(3):
                fields[0].setText(f2[i][0])
                fields.pop(0)

    def check(self):
        buttons = [self.radioButton_1, self.radioButton_2, self.radioButton_3, self.radioButton_4]
        if any(map(lambda x: x.isChecked(), buttons)):
            for i in buttons:
                if i.isChecked():
                    if i.objectName()[-1] == self.ans_field.objectName()[-1]:
                        self.right += 1
            if len(self.f1) > 0:
                self.fill_fields()
                self.messageLabel.setText('')
            else:
                self.result = Result(self.nickname, self.subject, self.name, self.right, len(self.f))
                self.close()
                self.result.show()
        else:
            self.messageLabel.setText('Не выбран вариант ответа!')


class Definition(QWidget, DefinitionUi):
    def __init__(self, nickname, subject, name, example=False, reverse=False):
        super(Definition, self).__init__()
        self.nickname = nickname
        self.subject = subject
        self.example = example
        self.name = name
        self.reverse = reverse
        self.right = 0
        self.setupUi(self)
        with open(f'data/{self.subject}/{self.name}.txt', encoding='utf-8') as f:
            self.f = list(map(lambda x: x.rstrip().split(' - '), f.readlines()))
        self.total = len(self.f)
        self.fill_fields()
        self.click_btn()

    def click_btn(self):
        self.backBtn.clicked.connect(self.back)
        if self.reverse:
            self.continueBtn.clicked.connect(self.check_term)
        else:
            self.continueBtn.clicked.connect(self.check_definition)

    def back(self):
        self.test_type = TestType(self.nickname, self.subject)
        self.close()
        self.test_type.show()

    def fill_fields(self):
        a = self.t, self.d = random.choice(self.f)
        self.f.remove(a)
        if self.reverse:
            self.definitionLabel.setText(self.d)
            self.termLabel.setReadOnly(False)
            self.definitionLabel.setReadOnly(True)
        else:
            self.termLabel.setText(self.t)
            self.definitionLabel.setReadOnly(False)
            self.termLabel.setReadOnly(True)

    def check_term(self):
        kal = self.termLabel.toPlainText()
        if len(kal) != 0:
            if kal.lower() == self.t.lower():
                self.right += 1
            if len(self.f) > 0:
                self.fill_fields()
                self.messageLabel.setText('')
                self.termLabel.setText('')
            else:
                print(self.right)
        else:
            self.messageLabel.setText('Напишите термин!')

    def check_definition(self):
        kal = list(set(map(lambda x: morph.parse(x.lower().strip('.,:;!?()%'))[0].normal_form,
                           sorted(self.definitionLabel.toPlainText().split()))))
        if len(kal) != 0:
            ideal = list(
                set(map(lambda x: morph.parse(x.lower().strip('.,:;!?()%'))[0].normal_form, sorted(self.d.split()))))
            same = 0
            for i in kal:
                if i in ideal:
                    same += 1
            percent = same / len(ideal) * 100
            if percent >= 50:
                self.right += 1
            if len(self.f) > 0:
                self.fill_fields()
                self.messageLabel.setText('')
                self.definitionLabel.setText('')
            else:
                self.result = Result(self.nickname, self.subject, self.name, self.right, self.total)
                self.close()
                self.result.show()
        else:
            self.messageLabel.setText('Напишите определение!')


class Test(QWidget, TestUi):
    def __init__(self, nickname, subject, name, example=False):
        super(Test, self).__init__()
        self.nickname = nickname
        self.subject = subject
        self.example = example
        self.name = name
        self.right = 0
        self.setupUi(self)
        with open(f'data/{self.subject}/{self.name}.txt', encoding='utf-8') as f:
            self.f = list(map(lambda x: x.rstrip().split(' - '), f.readlines()))
        self.total = len(self.f)
        self.fill_fields()
        self.click_btn()

    def click_btn(self):
        self.backBtn.clicked.connect(self.back)
        self.continueBtn.clicked.connect(self.check)

    def back(self):
        self.test_type = TestType(self.nickname, self.subject)
        self.close()
        self.test_type.show()

    def fill_fields(self):
        fields = [self.textEdit_1, self.textEdit_2, self.textEdit_3, self.textEdit_4]
        a = self.q, self.ans_vars = random.choice(self.f)
        self.questionText.setText(self.q)
        self.f.remove(a)
        self.right_ans, *self.wrong_ans = self.ans_vars.split(' | ')
        self.ans_field = random.choice(fields)
        self.ans_field.setText(str(self.right_ans))
        fields.remove(self.ans_field)
        for i in self.wrong_ans:
            fields[0].setText(str(i))
            fields.pop(0)

    def check(self):
        if any(map(lambda x: x.isChecked(), self.buttonGroup.buttons())):
            for i in self.buttonGroup.buttons():
                if i.isChecked():
                    if i.objectName()[-1] == self.ans_field.objectName()[-1]:
                        self.right += 1
            if len(self.f) > 0:
                self.fill_fields()
                self.messageLabel.setText('')
            else:
                self.result = Result(self.nickname, self.subject, self.name, self.right, self.total)
                self.close()
                self.result.show()
        else:
            self.messageLabel.setText('Не выбран вариант ответа!')


class PictureComparison(QWidget, PictureComparisonUi):
    def __init__(self, nickname, subject, name, example=False):
        super(PictureComparison, self).__init__()
        self.nickname = nickname
        self.subject = subject
        self.example = example
        self.name = name
        self.ans_field = None
        self.right = 0
        self.setupUi(self)
        with open(f'data/{self.subject}/{self.name}.txt', encoding='utf-8') as f:
            self.f = list(map(lambda x: x.rstrip().split(' - '), f.readlines()))
            self.f1 = self.f.copy()
        self.fill_fields()
        self.click_btn()

    def click_btn(self):
        self.backBtn.clicked.connect(self.back)
        self.continueBtn.clicked.connect(self.check)

    def back(self):
        self.test_type = TestType(self.nickname, self.subject)
        self.close()
        self.test_type.show()

    def fill_fields(self):
        widths = []
        f2 = self.f.copy()
        fields = [self.label_1, self.label_2, self.label_3, self.label_4]
        random.shuffle(fields)
        a = ex, ans = random.choice(self.f1)
        self.f1.remove(a)
        f2.remove(a)
        self.exerciseText.setText(ex)
        self.ans_field = random.choice(fields)
        self.pixmap = QtGui.QPixmap(ans)
        w, h = self.pixmap.size().width(), self.pixmap.size().height()
        widths.append(int(160 / h * w))
        self.ans_field.resize(int(160 / h * w), 160)
        self.ans_field.setPixmap(self.pixmap)
        fields.remove(self.ans_field)
        random.shuffle(f2)
        for i in range(3):
            pixmap = QtGui.QPixmap(f2[i][1])
            w, h = pixmap.size().width(), pixmap.size().height()
            widths.append(int(160 / h * w))
            fields[0].resize(int(160 / h * w), 160)
            fields[0].setPixmap(pixmap)
            fields.pop(0)
        self.setMaximumWidth(540 + max(widths) + 10)
        self.setMinimumWidth(540 + max(widths) + 10)

    def check(self):
        buttons = [self.radioButton_1, self.radioButton_2, self.radioButton_3, self.radioButton_4]
        if any(map(lambda x: x.isChecked(), buttons)):
            for i in buttons:
                if i.isChecked():
                    if i.objectName()[-1] == self.ans_field.objectName()[-1]:
                        self.right += 1
            if len(self.f1) > 0:
                self.fill_fields()
                self.messageLabel.setText('')
            else:
                self.result = Result(self.nickname, self.subject, self.name, self.right, len(self.f))
                self.close()
                self.result.show()
        else:
            self.messageLabel.setText('Не выбран вариант ответа!')


class Result(QWidget, ResultUi):
    def __init__(self, nickname, subject, name, right, total):
        super(Result, self).__init__()
        self.nickname = nickname
        self.subject = subject
        self.name = name
        self.right = right
        self.total = total
        with open(f'data/{self.subject}/{self.name}.txt', encoding='utf-8') as f:
            self.f = list(map(lambda x: x.rstrip(), f.readlines()))
        self.setupUi(self)
        self.fill()
        self.click_btn()

    def fill(self):
        self.rightLabel.setText(self.rightLabel.text() + f'{self.right} из {self.total}')
        percent = round((self.right / self.total) * 100)
        self.percent.setText(str(percent) + '%')
        self.scale.resize(percent * 3, 31)
        if percent <= 39:
            self.scale.setStyleSheet('''background-color: #FF0000;
                                    font: 13pt "MS Sans Serif";
                                    color: #808080;
                                    font-weight: 600;
                                    border-radius: 8px;
                                    border: 2px solid #000000;
                                    margin-top: 0px;
                                    outline: 0px;''')
            self.gradeLabel.setText(self.gradeLabel.text() + '2')
        elif 40 <= percent <= 64:
            self.scale.setStyleSheet('''background-color: #DAA520;
                                    font: 13pt "MS Sans Serif";
                                    color: #808080;
                                    font-weight: 600;
                                    border-radius: 8px;
                                    border: 2px solid #000000;
                                    margin-top: 0px;
                                    outline: 0px;''')
            self.gradeLabel.setText(self.gradeLabel.text() + '3')
        elif 65 <= percent <= 84:
            self.scale.setStyleSheet('''background-color: #00FF00;
                                    font: 13pt "MS Sans Serif";
                                    color: #808080;
                                    font-weight: 600;
                                    border-radius: 8px;
                                    border: 2px solid #000000;
                                    margin-top: 0px;
                                    outline: 0px;''')
            self.gradeLabel.setText(self.gradeLabel.text() + '4')
        elif percent >= 85:
            self.scale.setStyleSheet('''background-color: #008000;
                                    font: 13pt "MS Sans Serif";
                                    color: #808080;
                                    font-weight: 600;
                                    border-radius: 8px;
                                    border: 2px solid #000000;
                                    margin-top: 0px;
                                    outline: 0px;''')
            self.gradeLabel.setText(self.gradeLabel.text() + '5')

    def click_btn(self):
        self.continueBtn.clicked.connect(self.end)
        self.pushButton.clicked.connect(self.show_ans)

    def end(self):
        self.main = Main(self.nickname)
        self.close()
        self.main.show()

    def show_ans(self):
        self.ans = Answers(self.f)
        self.ans.show()


class Answers(QWidget, AnswersUi):
    def __init__(self, f):
        super(Answers, self).__init__()
        self.f = f
        self.model = QtGui.QStandardItemModel()
        self.setupUi(self)
        self.listView.setModel(self.model)
        self.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.fill()

    def fill(self):
        for i in self.f:
            i = i.split(' | ')[0]
            i = i.split()
            if len(i) >= 7:
                for j in range(7, len(i), 7):
                    i[j] = f'{i[j]}\n'
            i = ' '.join(i)
            i = QtGui.QStandardItem(i)
            self.model.appendRow(i)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Entrance()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
