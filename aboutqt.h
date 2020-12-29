#ifndef ABOUTQT_H
#define ABOUTQT_H

#include <QDialog>

namespace Ui {
class AboutQt;
}

class AboutQt : public QDialog
{
    Q_OBJECT

public:
    explicit AboutQt(QWidget *parent = nullptr);
    ~AboutQt();

private slots:
    void on_pushButton_2_clicked();

private:
    Ui::AboutQt *ui;
};

#endif // ABOUTQT_H
