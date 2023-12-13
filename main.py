from PyQt5.QtCore import Qt
import json
from PyQt5.QtWidgets import (QApplication, QWidget, QButtonGroup, QPushButton, QHBoxLayout, QVBoxLayout, QLabel,
                             QMessageBox, QRadioButton, QGroupBox, QLineEdit, QTextEdit, QListWidget)
import os

FILE_NAME = 'notes.json'

notes = {

    'Инструкция:':
        {
            'text': 'инструкция',
            'tags': ['круто', 'полезно', 'обучательно']
        },

    'заметка':
        {
            'text': 'заметка',
            'tags': ['прикольно', ' замечательно', 'плохо']
        }
}

app = QApplication([])

try:
    main_win = QWidget()
    main_win.setWindowTitle('Notes')
    main_win.resize(800, 400)

    text_field = QTextEdit()
    text_field.setPlaceholderText('Enter note text')
    notes_Label = QLabel('List of notes')
    tags_Label = QLabel('List of Tags')
    notes_list_widget = QListWidget()
    tags_list_widget = QListWidget()
    search_line_widget = QLineEdit()

    search_line_widget.setPlaceholderText('Search for...')
    create_note_button = QPushButton('Create note')
    delete_note_button = QPushButton('Delete note')
    save_note_button = QPushButton('Save note')
    add_to_note_button = QPushButton('Add to note')
    remove_tag_button = QPushButton('Remove from note')
    search_button = QPushButton('Search by tag')
    end_search_button = QPushButton('End search')
    main_layout = QHBoxLayout()
    sub_layout1 = QVBoxLayout()
    sub_layout2 = QVBoxLayout()
    child_layout1 = QHBoxLayout()
    child_layout2 = QHBoxLayout()
    child_layout3 = QHBoxLayout()
    child_layout4 = QHBoxLayout()
    child_layout5 = QHBoxLayout()
    child_layout6 = QHBoxLayout()
    child_layout7 = QHBoxLayout()

    enter_note_name = QLineEdit()
    enter_tag_name = QLineEdit()

    main_layout.addLayout(sub_layout1)
    main_layout.addLayout(sub_layout2)
    sub_layout1.addWidget(text_field)
    sub_layout2.addWidget(notes_Label)
    sub_layout2.addWidget(notes_list_widget)
    sub_layout2.addWidget(enter_note_name)
    sub_layout2.addWidget(search_line_widget)
    sub_layout2.addWidget(search_button)
    sub_layout2.addWidget(end_search_button)
    sub_layout2.addLayout(child_layout1)
    child_layout1.addWidget(create_note_button)
    child_layout1.addWidget(delete_note_button)
    sub_layout2.addWidget(save_note_button)
    sub_layout2.addWidget(tags_Label)
    sub_layout2.addWidget(tags_list_widget)
    sub_layout2.addWidget(enter_tag_name)
    sub_layout2.addLayout(child_layout2)
    child_layout2.addWidget(add_to_note_button)
    child_layout2.addWidget(remove_tag_button)

    main_win.setLayout(main_layout)
    enter_note_name.setPlaceholderText('Enter note name')
    enter_tag_name.setPlaceholderText('Enter tag name')
except:
    pass
def end_search():
    notes_list_widget.clear()
    notes_list_widget.addItems(notes)
def show_searched_notes():
    searched_notes = []
    if search_line_widget != '':
        for i in notes.keys():
            if search_line_widget.text() in notes[i]['tags']:
                searched_notes.append(i)
            notes_list_widget.clear()
            notes_list_widget.addItems(searched_notes)
        search_line_widget.clear()



def show_note():
    name = notes_list_widget.selectedItems()[0].text()
    text_field.setText(notes[name]['text'])
    tags_list_widget.clear()
    tags_list_widget.addItems(notes[name]['tags'])

def add_note():
    if enter_note_name.text() in notes or enter_note_name.text() == '':
        message_box = QMessageBox()
        message_box.setText('Incorrect name')
        message_box.exec_()
    else:
        notes[enter_note_name.text()] = {'text': '','tags': []}
        with open(FILE_NAME, 'w', encoding='utf-8') as file:
            json.dump(notes, file, sort_keys=True)
        notes_list_widget.clear()
        notes_list_widget.addItems(notes)
        enter_note_name.clear()
def delete_note():

    if notes_list_widget.selectedItems() != []:
        name = notes_list_widget.selectedItems()[0].text()
        del notes[name]
    else:
        message_box = QMessageBox()
        message_box.setText('No note selected')
        message_box.exec_()
    with open(FILE_NAME, 'w', encoding='utf-8') as file:
        json.dump(notes, file, sort_keys=True)
    notes_list_widget.clear()
    notes_list_widget.addItems(notes)

def save_note():
    name = notes_list_widget.selectedItems()[0].text()
    if text_field.toPlainText() != '':
        notes[name]['text'] = text_field.toPlainText()
        with open(FILE_NAME, 'w', encoding='utf-8') as file:
            json.dump(notes, file, sort_keys=True)
    else:
        message_box = QMessageBox()
        message_box.setText('No text')
        message_box.exec_()


if os.path.isfile(FILE_NAME):
    with open(FILE_NAME, 'r', encoding='utf-8') as file:
        notes = json.load(file)

else:
    with open(FILE_NAME, 'w', encoding='utf-8') as file:
        json.dump(notes, file, sort_keys=True)

def remove_tag():
    tag_name = enter_tag_name.text()
    note_name = notes_list_widget.selectedItems()[0].text()
    notes[note_name]['tags'].remove(tags_list_widget.selectedItems()[0].text())
    tags_list_widget.clear()
    tags_list_widget.addItems(notes[note_name]['tags'])
    with open(FILE_NAME, 'w', encoding='utf-8') as file:
        json.dump(notes, file, sort_keys=True)
def add_tag():
    if notes_list_widget.selectedItems() == []:
        message_box = QMessageBox()
        message_box.setText('No note selected')
        message_box.exec_()
    tag_name = enter_tag_name.text()
    note_name = notes_list_widget.selectedItems()[0].text()
    print(note_name)
    print(tag_name)
    if (not tag_name in notes[note_name]['tags']) and tag_name != '':
        print('print')
        notes[note_name]['tags'].append(tag_name)
        print('print')
        tags_list_widget.clear()
        tags_list_widget.addItems(notes[note_name]['tags'])
        with open(FILE_NAME, 'w', encoding='utf-8') as file:
            json.dump(notes, file, sort_keys=True)
        enter_tag_name.clear()
    else:
        message_box = QMessageBox()
        message_box.setText('Incorrect name')
        message_box.exec_()





notes_list_widget.addItems(notes)
notes_list_widget.itemClicked.connect(show_note)

create_note_button.clicked.connect(add_note)
save_note_button.clicked.connect(save_note)
delete_note_button.clicked.connect(delete_note)
add_to_note_button.clicked.connect(add_tag)
remove_tag_button.clicked.connect(remove_tag)
search_button.clicked.connect(show_searched_notes)
end_search_button.clicked.connect(end_search)
main_win.show()
app.exec_()
