# -*- coding: utf-8 -*-



# Form implementation generated from reading ui file 'morph/readability_settings.ui'

#

# Created by: PyQt5 UI code generator 5.15.1

#

# WARNING: Any manual changes made to this file will be lost when pyuic5 is

# run again.  Do not edit this file unless you know what you are doing.





from PyQt5 import QtCore, QtGui, QtWidgets





class Ui_ReadabilitySettingsDialog(object):

    def setupUi(self, ReadabilitySettingsDialog):

        ReadabilitySettingsDialog.setObjectName("ReadabilitySettingsDialog")

        ReadabilitySettingsDialog.resize(377, 340)

        ReadabilitySettingsDialog.setSizeGripEnabled(False)

        ReadabilitySettingsDialog.setModal(True)

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(ReadabilitySettingsDialog)

        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.studyPlanGroup = QtWidgets.QGroupBox(ReadabilitySettingsDialog)

        self.studyPlanGroup.setObjectName("studyPlanGroup")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.studyPlanGroup)

        self.verticalLayout.setObjectName("verticalLayout")

        self.alwaysAddMinimumFreqCheckBox = QtWidgets.QCheckBox(self.studyPlanGroup)

        self.alwaysAddMinimumFreqCheckBox.setMinimumSize(QtCore.QSize(0, 0))

        self.alwaysAddMinimumFreqCheckBox.setObjectName("alwaysAddMinimumFreqCheckBox")

        self.verticalLayout.addWidget(self.alwaysAddMinimumFreqCheckBox)

        self.alwaysMeetReadTargettCheckBox = QtWidgets.QCheckBox(self.studyPlanGroup)

        self.alwaysMeetReadTargettCheckBox.setMinimumSize(QtCore.QSize(0, 0))

        self.alwaysMeetReadTargettCheckBox.setObjectName("alwaysMeetReadTargettCheckBox")

        self.verticalLayout.addWidget(self.alwaysMeetReadTargettCheckBox)

        self.verticalLayout_3.addWidget(self.studyPlanGroup)

        self.frequencyListGroup = QtWidgets.QGroupBox(ReadabilitySettingsDialog)

        self.frequencyListGroup.setObjectName("frequencyListGroup")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frequencyListGroup)

        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.fillAllMorphsCheckBox = QtWidgets.QCheckBox(self.frequencyListGroup)

        self.fillAllMorphsCheckBox.setMinimumSize(QtCore.QSize(0, 0))

        self.fillAllMorphsCheckBox.setStatusTip("")

        self.fillAllMorphsCheckBox.setObjectName("fillAllMorphsCheckBox")

        self.verticalLayout_2.addWidget(self.fillAllMorphsCheckBox)

        self.verticalLayout_3.addWidget(self.frequencyListGroup)

        self.wordReportGroup = QtWidgets.QGroupBox(ReadabilitySettingsDialog)

        self.wordReportGroup.setObjectName("wordReportGroup")

        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.wordReportGroup)

        self.verticalLayout_5.setObjectName("verticalLayout_5")

        self.saveMissingWordsCheckBox = QtWidgets.QCheckBox(self.wordReportGroup)

        self.saveMissingWordsCheckBox.setObjectName("saveMissingWordsCheckBox")

        self.verticalLayout_5.addWidget(self.saveMissingWordsCheckBox)

        self.saveReadabilityDBCheckBox = QtWidgets.QCheckBox(self.wordReportGroup)

        self.saveReadabilityDBCheckBox.setObjectName("saveReadabilityDBCheckBox")

        self.verticalLayout_5.addWidget(self.saveReadabilityDBCheckBox)

        self.verticalLayout_3.addWidget(self.wordReportGroup)

        self.extrasGroup = QtWidgets.QGroupBox(ReadabilitySettingsDialog)

        self.extrasGroup.setObjectName("extrasGroup")

        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.extrasGroup)

        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.migakuDictionaryTagsCheckBox = QtWidgets.QCheckBox(self.extrasGroup)

        self.migakuDictionaryTagsCheckBox.setChecked(False)

        self.migakuDictionaryTagsCheckBox.setObjectName("migakuDictionaryTagsCheckBox")

        self.verticalLayout_4.addWidget(self.migakuDictionaryTagsCheckBox)

        self.webServiceCheckBox = QtWidgets.QCheckBox(self.extrasGroup)

        self.webServiceCheckBox.setMinimumSize(QtCore.QSize(0, 0))

        self.webServiceCheckBox.setStatusTip("")

        self.webServiceCheckBox.setObjectName("webServiceCheckBox")

        self.verticalLayout_4.addWidget(self.webServiceCheckBox)

        self.verticalLayout_3.addWidget(self.extrasGroup)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(spacerItem)

        self.buttonBox = QtWidgets.QDialogButtonBox(ReadabilitySettingsDialog)

        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)

        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)

        self.buttonBox.setObjectName("buttonBox")

        self.verticalLayout_3.addWidget(self.buttonBox)



        self.retranslateUi(ReadabilitySettingsDialog)

        self.buttonBox.accepted.connect(ReadabilitySettingsDialog.accept)

        self.buttonBox.rejected.connect(ReadabilitySettingsDialog.reject)

        QtCore.QMetaObject.connectSlotsByName(ReadabilitySettingsDialog)



    def retranslateUi(self, ReadabilitySettingsDialog):

        _translate = QtCore.QCoreApplication.translate

        ReadabilitySettingsDialog.setWindowTitle(_translate("ReadabilitySettingsDialog", "Advanced Settings"))

        self.studyPlanGroup.setTitle(_translate("ReadabilitySettingsDialog", "Study Plan"))

        self.alwaysAddMinimumFreqCheckBox.setToolTip(_translate("ReadabilitySettingsDialog", "Always add Minimum Frequency morphs to the study plan,\n"

"even if it exceeds the readability \'Target %\'."))

        self.alwaysAddMinimumFreqCheckBox.setText(_translate("ReadabilitySettingsDialog", "Always add Minimum Frequency morphs"))

        self.alwaysMeetReadTargettCheckBox.setToolTip(_translate("ReadabilitySettingsDialog", "Always add enough morphs to the Study Plan to meet the readability \'Target %\'\n"

"even if morphemes are below the \'Minimum Frequency\'.\n"

"\n"

"\'Minimum Frequency\' morphs still take priority."))

        self.alwaysMeetReadTargettCheckBox.setText(_translate("ReadabilitySettingsDialog", "Always meet Target %"))

        self.frequencyListGroup.setTitle(_translate("ReadabilitySettingsDialog", "Frequency Lists"))

        self.fillAllMorphsCheckBox.setToolTip(_translate("ReadabilitySettingsDialog", "When generating a study plan, by default only those morphemes that are in the plan are added to your \'frequency.txt\'.\n"

"This option includes all other morphemes at the your frequency list, enabling you to study ahead if desired."))

        self.fillAllMorphsCheckBox.setText(_translate("ReadabilitySettingsDialog", "Add all missing morphemes at the end of the Frequency List"))

        self.wordReportGroup.setTitle(_translate("ReadabilitySettingsDialog", "Word Reports"))

        self.saveMissingWordsCheckBox.setToolTip(_translate("ReadabilitySettingsDialog", "Save a report including any unknown morphs in the Master Frequency List.\n"

"\n"

"Outputs:\n"

" - missing_master_word_report.txt"))

        self.saveMissingWordsCheckBox.setText(_translate("ReadabilitySettingsDialog", "Save Missing Words Report"))

        self.saveReadabilityDBCheckBox.setToolTip(_translate("ReadabilitySettingsDialog", "Generare a readability corpus database.\n"

"\n"

"Outputs:\n"

" - word_corpus.corpusdb"))

        self.saveReadabilityDBCheckBox.setText(_translate("ReadabilitySettingsDialog", "Save Readability Corpus DB"))

        self.extrasGroup.setTitle(_translate("ReadabilitySettingsDialog", "Extras"))

        self.migakuDictionaryTagsCheckBox.setToolTip(_translate("ReadabilitySettingsDialog", "Add MorphMan frequency tags to Migaku Dictionary entries.\n"

"Requires Migaku Dictionary to be installed."))

        self.migakuDictionaryTagsCheckBox.setText(_translate("ReadabilitySettingsDialog", "Migaku Dictionary Tags"))

        self.webServiceCheckBox.setToolTip(_translate("ReadabilitySettingsDialog", "Enables a WebSocket Service, allowing external apps to use MorphMan services.\n"

"Requires re-opening the Readability Analyzer to take effect."))

        self.webServiceCheckBox.setText(_translate("ReadabilitySettingsDialog", "Enable Web Service (beta)"))

