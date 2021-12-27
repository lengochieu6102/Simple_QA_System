# Bài tập lớn Xử lý Ngôn ngữ Tự nhiên - HK211
## Natural Language Processing Assignment - Term-211
**Student Name**: Lê Ngọc Hiếu\
**Student ID**: 1812164
## Đề bài - Topic
Xây dựng hệ thống hỏi đáp đơn giản về các chuyến tàu hỏa liên tỉnh bằng Quan hệ văn phạm.

Build simple Vietnamese Question-Answering System for retrieving information of inter-province train system by using Relational Grammar.

## Cơ sở dữ liệu - Database
### Cho cơ sở dữ liệu của các chuyến tàu hỏa:

(TRAIN B1) (TRAIN B2) (TRAIN B3)\
(TRAIN B4) (TRAIN B5) (TRAIN B6)

(ATIME B1 HUE 19:00HR)\
(ATIME B2 HUE 22:30HR)\
(ATIME B3 HCMC 16:00HR)\
(ATIME B4 NTrang 16:30HR)\
(ATIME B5 HN 23:30HR)\
(ATIME B6 DANANG 11:30HR)

(DTIME B1 HCMC 10:00HR)\
(DTIME B2 HN 14:30HR)\
(DTIME B3 DANANG 6:00HR)\
(DTIME B4 DANANG 8:30HR)\
(DTIME B5 HCMC 3:30HR)\
(DTIME B6 HUE 7:30HR)

(RUN-TIME B1 HCMC HUE 9:00HR)\
(RUN-TIME B2 HN HUE 8:00HR)\
(RUN-TIME B3 DANANG HCMC 10:00HR)\
(RUN-TIME B4 DANANG NTrang 8:00HR)\
(RUN-TIME B5 HCMC HN 18:00HR)\
(RUN-TIME B6 HUE DANANG 4:00HR)

## Yêu cầu - Requirements
### Câu truy vấn - Query Sentences
i) Tàu hỏa nào đến thành phố Huế lúc 19:00HR ?\
ii) Thời gian tàu hỏa B3 chạy từ Đà Nẵng đến TP. Hồ Chí Minh là mấy giờ?\
iii) Tàu hỏa nào đến thành phố Hồ Chí Minh ?\
iv) Tàu hỏa nào chạy từ Nha Trang, lúc mấy giờ\
v) Tàu hỏa nào chạy từ TP.Hồ Chí Minh đến Hà Nội ?\
vi) Tàu hỏa B5 có chạy từ Đà Nẵng không ?

### Câu hỏi theo quy trình - Processes
a) Xây dựng bộ phân tích cú pháp của văn phạm phụ thuộc.\
b) Phân tích cú pháp và xuất ra các quan hệ ngữ nghĩa của các câu truy vấn.\
c) Từ kết quả ở b) tạo các quan hệ văn phạm cho về các chuyến tàu hỏa giữa thành phố Hồ Chí Minh, Huế, Đà Nẵng, Nha Trang và Hà Nội \với cơ sở dữ liệu đã cho ở trên.\
d) Tạo dạng luận lý từ các quan hệ văn phạm ở c).\
e) Tạo ngữ nghĩa thủ tục từ dạng luận lý ở d).\
f) Truy xuất dữ liệu để tìm thông tin trả lời cho các câu truy vấn trên.

### Yêu cầu khi thực thi - Environments
#### a. Ngôn ngữ sử dụng - Language: 
Python 3.7
#### b. Cấu trúc files - Structures:
Gồm 1 file python ngoài cùng:
- main.py: Điểm bắt đầu của chương trình, sử dụng optparse để parse các input và output\

Folder:
- Input chứa các file input cho các câu hỏi đầu vào của bài toán.
- Output chứa các file output kết quả thực thi của mỗi câu hỏi, output của yêu cầu trước sẽ là input của yêu cầu sau.
- Models: chứa các lớp hoặc các module con thực thi bài toán. Ngoài ra còn chứa file ngữ pháp grammar.cfg và file dữ liệu database.txt

## Hướng dẫn chạy chương trình - Run Program
```sh
$ python main.py --input-file INPUT_FILE [--input-directory INPUT_ROOT]
```
Ví dụ
```sh
$ python main.py --input-file input_2.txt
```
## Link github:
https://github.com/lengochieu6102/NLP_Simple_QA_System.git
