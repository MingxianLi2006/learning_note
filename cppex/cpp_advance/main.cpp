#include <opencv2/opencv.hpp>
#include <iostream>
int main()
{
    cv::Mat img=cv::imread("1.png");
    cv::imshow("hello",img);
    cv::waitKey(0);
    return 0;
}