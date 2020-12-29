QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

CONFIG += c++11

# You can make your code fail to compile if it uses deprecated APIs.
# In order to do so, uncomment the following line.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

DEFINES += VERSION="1.0"

win32:{
    RC_ICONS = $$PWD/qtcalc.ico
    VERSION = 1.0
    QMAKE_TARGET_COMPANY = jDan735
    QMAKE_TARGET_PRODUCT = QtCalc
    QMAKE_TARGET_DESCRIPTION = QtCalc
    QMAKE_TARGET_COPYRIGHT = jDan735
}

SOURCES += \
    aboutqt.cpp \
    main.cpp \
    mainwindow.cpp

HEADERS += \
    aboutqt.h \
    mainwindow.h

FORMS += \
    aboutqt.ui \
    mainwindow.ui

# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target

RESOURCES += \
    resources.qrc