#include "mainwindow.h"
#include "aboutqt.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    connect(ui->actionAbout_Qt, &QAction::triggered, this, &MainWindow::showAboutQt);
}

void MainWindow::showAboutQt(){
    AboutQt *popup = new AboutQt(this);
    popup->setModal(true);
    popup->show();
}

MainWindow::~MainWindow()
{
    delete ui;
}

