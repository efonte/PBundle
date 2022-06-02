# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(980, 600)
        MainWindow.setMinimumSize(QtCore.QSize(980, 600))
        MainWindow.setMaximumSize(QtCore.QSize(980, 600))
        MainWindow.setAcceptDrops(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(10, 10, 761, 541))
        self.treeWidget.setMaximumSize(QtCore.QSize(761, 541))
        self.treeWidget.setToolTip("")
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.treeWidget.setAnimated(True)
        self.treeWidget.setAllColumnsShowFocus(True)
        self.treeWidget.setHeaderHidden(False)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "None")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.treeWidget.headerItem().setFont(0, font)
        self.treeWidget.header().setVisible(True)
        self.pb_delete_file = QtWidgets.QPushButton(self.centralwidget)
        self.pb_delete_file.setEnabled(False)
        self.pb_delete_file.setGeometry(QtCore.QRect(790, 40, 171, 23))
        self.pb_delete_file.setToolTip("")
        self.pb_delete_file.setObjectName("pb_delete_file")
        self.pb_add_file = QtWidgets.QPushButton(self.centralwidget)
        self.pb_add_file.setEnabled(False)
        self.pb_add_file.setGeometry(QtCore.QRect(790, 10, 81, 23))
        self.pb_add_file.setToolTip("")
        self.pb_add_file.setObjectName("pb_add_file")
        self.pb_extract_file = QtWidgets.QPushButton(self.centralwidget)
        self.pb_extract_file.setEnabled(False)
        self.pb_extract_file.setGeometry(QtCore.QRect(790, 70, 81, 23))
        self.pb_extract_file.setToolTip("")
        self.pb_extract_file.setObjectName("pb_extract_file")
        self.pb_add_folder = QtWidgets.QPushButton(self.centralwidget)
        self.pb_add_folder.setEnabled(False)
        self.pb_add_folder.setGeometry(QtCore.QRect(880, 10, 81, 23))
        self.pb_add_folder.setToolTip("")
        self.pb_add_folder.setObjectName("pb_add_folder")
        self.pb_replace_file = QtWidgets.QPushButton(self.centralwidget)
        self.pb_replace_file.setEnabled(False)
        self.pb_replace_file.setGeometry(QtCore.QRect(880, 70, 81, 23))
        self.pb_replace_file.setToolTip("")
        self.pb_replace_file.setObjectName("pb_replace_file")
        self.l1 = QtWidgets.QFrame(self.centralwidget)
        self.l1.setGeometry(QtCore.QRect(790, 130, 171, 20))
        self.l1.setToolTip("")
        self.l1.setFrameShape(QtWidgets.QFrame.HLine)
        self.l1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.l1.setObjectName("l1")
        self.le_size = QtWidgets.QLineEdit(self.centralwidget)
        self.le_size.setEnabled(True)
        self.le_size.setGeometry(QtCore.QRect(800, 160, 151, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(84, 84, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 56, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(84, 84, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 56, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.le_size.setPalette(palette)
        self.le_size.setMouseTracking(False)
        self.le_size.setAcceptDrops(False)
        self.le_size.setToolTip("<html><head/><body><p>None</p></body></html>")
        self.le_size.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.le_size.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.le_size.setReadOnly(True)
        self.le_size.setObjectName("le_size")
        self.le_crc = QtWidgets.QLineEdit(self.centralwidget)
        self.le_crc.setEnabled(True)
        self.le_crc.setGeometry(QtCore.QRect(800, 190, 151, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 56, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 56, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.le_crc.setPalette(palette)
        self.le_crc.setMouseTracking(False)
        self.le_crc.setAcceptDrops(False)
        self.le_crc.setToolTip("<html><head/><body><p>None</p></body></html>")
        self.le_crc.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.le_crc.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.le_crc.setReadOnly(True)
        self.le_crc.setObjectName("le_crc")
        self.text_size = QtWidgets.QLabel(self.centralwidget)
        self.text_size.setGeometry(QtCore.QRect(810, 160, 30, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(68, 68, 68))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 68, 68))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.text_size.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.text_size.setFont(font)
        self.text_size.setToolTip("")
        self.text_size.setObjectName("text_size")
        self.text_crc = QtWidgets.QLabel(self.centralwidget)
        self.text_crc.setGeometry(QtCore.QRect(810, 190, 30, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(68, 68, 68))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 68, 68))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.text_crc.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.text_crc.setFont(font)
        self.text_crc.setToolTip("")
        self.text_crc.setObjectName("text_crc")
        self.pb_open = QtWidgets.QPushButton(self.centralwidget)
        self.pb_open.setEnabled(False)
        self.pb_open.setGeometry(QtCore.QRect(790, 250, 171, 31))
        self.pb_open.setToolTip("<html><head/><body><p>Open a bnd or gzipped file inside the current file</p></body></html>")
        self.pb_open.setCheckable(False)
        self.pb_open.setObjectName("pb_open")
        self.l2 = QtWidgets.QFrame(self.centralwidget)
        self.l2.setGeometry(QtCore.QRect(790, 220, 171, 20))
        self.l2.setToolTip("")
        self.l2.setFrameShape(QtWidgets.QFrame.HLine)
        self.l2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.l2.setObjectName("l2")
        self.pb_movedown = QtWidgets.QPushButton(self.centralwidget)
        self.pb_movedown.setEnabled(False)
        self.pb_movedown.setGeometry(QtCore.QRect(790, 100, 81, 23))
        self.pb_movedown.setToolTip("")
        self.pb_movedown.setAutoRepeat(True)
        self.pb_movedown.setObjectName("pb_movedown")
        self.pb_moveup = QtWidgets.QPushButton(self.centralwidget)
        self.pb_moveup.setEnabled(False)
        self.pb_moveup.setGeometry(QtCore.QRect(880, 100, 81, 23))
        self.pb_moveup.setToolTip("")
        self.pb_moveup.setAutoRepeat(True)
        self.pb_moveup.setObjectName("pb_moveup")
        self.pb_back = QtWidgets.QPushButton(self.centralwidget)
        self.pb_back.setEnabled(False)
        self.pb_back.setGeometry(QtCore.QRect(790, 290, 171, 31))
        self.pb_back.setToolTip("<html><head/><body><p>Return back to the previous file. Changes are only applied if the current file is saved.</p></body></html>")
        self.pb_back.setObjectName("pb_back")
        self.l3 = QtWidgets.QFrame(self.centralwidget)
        self.l3.setGeometry(QtCore.QRect(790, 330, 171, 20))
        self.l3.setToolTip("")
        self.l3.setFrameShape(QtWidgets.QFrame.HLine)
        self.l3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.l3.setObjectName("l3")
        self.te_preview = QtWidgets.QTextEdit(self.centralwidget)
        self.te_preview.setEnabled(True)
        self.te_preview.setGeometry(QtCore.QRect(800, 360, 151, 191))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(84, 84, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 56, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(84, 84, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 56, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.te_preview.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.te_preview.setFont(font)
        self.te_preview.setAcceptDrops(False)
        self.te_preview.setToolTip("<html><head/><body><p>Files that start with <span style=\" font-weight:600;\">42 4E 44</span> are bnd files. Files that start with <span style=\" font-weight:600;\">1F 0B 08</span> are gzipped files.</p></body></html>")
        self.te_preview.setUndoRedoEnabled(False)
        self.te_preview.setReadOnly(True)
        self.te_preview.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.te_preview.setObjectName("te_preview")
        self.le_preview = QtWidgets.QLabel(self.centralwidget)
        self.le_preview.setEnabled(True)
        self.le_preview.setGeometry(QtCore.QRect(800, 360, 151, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(68, 68, 68))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 68, 68))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.le_preview.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setItalic(True)
        self.le_preview.setFont(font)
        self.le_preview.setToolTip("")
        self.le_preview.setAlignment(QtCore.Qt.AlignCenter)
        self.le_preview.setObjectName("le_preview")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 980, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuActions = QtWidgets.QMenu(self.menubar)
        self.menuActions.setObjectName("menuActions")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_load = QtWidgets.QAction(MainWindow)
        self.action_load.setObjectName("action_load")
        self.action_save = QtWidgets.QAction(MainWindow)
        self.action_save.setObjectName("action_save")
        self.action_refresh = QtWidgets.QAction(MainWindow)
        self.action_refresh.setObjectName("action_refresh")
        self.action_exit = QtWidgets.QAction(MainWindow)
        self.action_exit.setObjectName("action_exit")
        self.action_save_as = QtWidgets.QAction(MainWindow)
        self.action_save_as.setEnabled(False)
        self.action_save_as.setObjectName("action_save_as")
        self.action_disable_filesystem_and_save = QtWidgets.QAction(MainWindow)
        self.action_disable_filesystem_and_save.setEnabled(False)
        self.action_disable_filesystem_and_save.setObjectName("action_disable_filesystem_and_save")
        self.action_overwrite_all_filenames = QtWidgets.QAction(MainWindow)
        self.action_overwrite_all_filenames.setEnabled(False)
        self.action_overwrite_all_filenames.setObjectName("action_overwrite_all_filenames")
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.check_reload_on_save = QtWidgets.QAction(MainWindow)
        self.check_reload_on_save.setCheckable(True)
        self.check_reload_on_save.setObjectName("check_reload_on_save")
        self.check_extended_backup_files = QtWidgets.QAction(MainWindow)
        self.check_extended_backup_files.setCheckable(True)
        self.check_extended_backup_files.setObjectName("check_extended_backup_files")
        self.check_encryption_decryption = QtWidgets.QAction(MainWindow)
        self.check_encryption_decryption.setCheckable(False)
        self.check_encryption_decryption.setEnabled(False)
        self.check_encryption_decryption.setObjectName("check_encryption_decryption")
        self.check_external_header_file = QtWidgets.QAction(MainWindow)
        self.check_external_header_file.setCheckable(True)
        self.check_external_header_file.setEnabled(False)
        self.check_external_header_file.setObjectName("check_external_header_file")
        self.menuFile.addAction(self.action_load)
        self.menuFile.addAction(self.action_save)
        self.menuFile.addAction(self.action_save_as)
        self.menuFile.addAction(self.action_refresh)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_exit)
        self.menuHelp.addAction(self.action_about)
        self.menuActions.addAction(self.action_disable_filesystem_and_save)
        self.menuActions.addAction(self.action_overwrite_all_filenames)
        self.menuSettings.addAction(self.check_reload_on_save)
        self.menuSettings.addAction(self.check_extended_backup_files)
        self.menuSettings.addAction(self.check_encryption_decryption)
        self.menuSettings.addAction(self.check_external_header_file)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuActions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Patapon BND Editor"))
        self.treeWidget.setSortingEnabled(False)
        self.pb_delete_file.setText(_translate("MainWindow", "Delete file(s)"))
        self.pb_add_file.setText(_translate("MainWindow", "Add file(s)"))
        self.pb_extract_file.setText(_translate("MainWindow", "Extract file(s)"))
        self.pb_add_folder.setText(_translate("MainWindow", "Add folder"))
        self.pb_replace_file.setText(_translate("MainWindow", "Replace file(s)"))
        self.le_size.setText(_translate("MainWindow", "Size "))
        self.le_crc.setText(_translate("MainWindow", "CRC "))
        self.text_size.setText(_translate("MainWindow", "Size"))
        self.text_crc.setText(_translate("MainWindow", "CRC"))
        self.pb_open.setText(_translate("MainWindow", "Open local .BND file (→)"))
        self.pb_open.setShortcut(_translate("MainWindow", "Right"))
        self.pb_movedown.setText(_translate("MainWindow", "Move down"))
        self.pb_moveup.setText(_translate("MainWindow", "Move up"))
        self.pb_back.setText(_translate("MainWindow", "Back to previous file (←)"))
        self.pb_back.setShortcut(_translate("MainWindow", "Left"))
        self.te_preview.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto Mono\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"><br /></p></body></html>"))
        self.le_preview.setText(_translate("MainWindow", "Preview (first 0x70 bytes)"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuActions.setTitle(_translate("MainWindow", "Actions"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.action_load.setText(_translate("MainWindow", "Load"))
        self.action_load.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.action_save.setText(_translate("MainWindow", "Save"))
        self.action_save.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action_refresh.setText(_translate("MainWindow", "Refresh"))
        self.action_refresh.setShortcut(_translate("MainWindow", "F5"))
        self.action_exit.setText(_translate("MainWindow", "Exit"))
        self.action_save_as.setText(_translate("MainWindow", "Save as"))
        self.action_disable_filesystem_and_save.setText(_translate("MainWindow", "Disable filesystem and save"))
        self.action_overwrite_all_filenames.setText(_translate("MainWindow", "Overwrite all filenames"))
        self.action_about.setText(_translate("MainWindow", "About"))
        self.check_reload_on_save.setText(_translate("MainWindow", "Reload on save"))
        self.check_extended_backup_files.setText(_translate("MainWindow", "Disable backups"))
        self.check_encryption_decryption.setText(_translate("MainWindow", "Encryption / decryption"))
        self.check_external_header_file.setText(_translate("MainWindow", "External header file"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())