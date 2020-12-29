#include "aboutqt.h"
#include "ui_aboutqt.h"

AboutQt::AboutQt(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::AboutQt)
{
    ui->setupUi(this);
    QString qtver = "Version " + QString::number(QT_VERSION_MAJOR) + "." + QString::number(QT_VERSION_MINOR) + "." + QString::number(QT_VERSION_PATCH);
    ui->label_3->setText(qtver);
}

AboutQt::~AboutQt()
{
    delete ui;
}

void AboutQt::on_pushButton_2_clicked()
{
    accept();
}
