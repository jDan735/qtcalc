#include "aboutapp.h"
#include "ui_aboutapp.h"

#include <string>

AboutApp::AboutApp(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::AboutApp)
{
    ui->setupUi(this);
    QString ver = "Version " + QString::number(VERSION);
    ui->label_3->setText(ver);
}

AboutApp::~AboutApp()
{
    delete ui;
}

void AboutApp::on_pushButton_clicked()
{
    accept();
}
