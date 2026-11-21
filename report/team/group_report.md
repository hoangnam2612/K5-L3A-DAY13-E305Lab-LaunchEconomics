# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: E305Lab
- Lớp: L3A
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

LogiX-VN (12 depot, khoảng 45.000 yêu cầu hoàn phí mỗi tháng) muốn mở pilot trợ lý hoàn phí. Nhóm trả lời bốn câu: có đáng chạy không, nhân viên có dùng không, khi hỏng thì sao, và pilot thiết kế thế nào để ra được quyết định. Cách tiếp cận: tính chi phí thật từ trace (mọi lần chạy, kể cả lần lỗi, cộng giờ nhân viên), thử độ nhạy, phân loại lỗi, rồi thiết kế pilot đủ cỡ mẫu có luật dừng viết trước. Toàn bộ dữ liệu là giả lập; mọi số tính từ hai cột `_simulated` đều ghi nhãn simulated.

## 3. Giải pháp

Tóm tắt cách nhóm làm từng nhiệm vụ A–E và link tới file hồ sơ tương ứng.

- **A · Mô hình chi phí** (`src/lab13.py`, `report/team/bang_chi_phi.md`): ba hàm kinh tế của việc chạy lại đạt ba phép thử (1,20 · 1,25 · 1,25); `mo_hinh` tính chi phí từ trace, tách theo loại yêu cầu (A3) và cộng chi phí cố định (A4).
- **B · Độ nhạy** (`bang_chi_phi.md`): gọi lại `mo_hinh` cho 9 kịch bản đổi từng yếu tố, một cặp, giới hạn 1–3 lần chạy tính chi phí cả hệ thống, và kịch bản xem lại 100%.
- **C · Bảng lỗi** (`report/team/bang_loi.md`): hai thành viên gắn nhãn độc lập 20 ca theo năm loại của Google PAIR, đồng thuận 17/20 = 85%; viết quy tắc cho 3 ca lệch (4, 16, 18) và khắc phục 5 ca, mỗi loại một ca.
- **D · Pilot** (`report/team/pilot_plan.yaml`, khối D1 trong `src/lab13.py`): tính cỡ mẫu cho ba cách chia, chọn chia theo nhân viên 20 + 20, viết ba luật dừng đủ bốn vế.
- **E · Chỉ số và hồ sơ** (`report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`): ba chỉ số tính thử, chín event có `trace_id`, ba dòng rủi ro kinh tế, hồ sơ một trang bảy mục.

## 4. Kết quả

Con số chính (ghi nhãn `simulated` khi cần) và đề xuất cuối của `ho_so_launch_v0.md`. Kết quả duyệt chéo nhóm nhận được từ hội đồng.

- Chi phí mỗi việc thành công **4.472 đ** [simulated], gấp **16,3 lần** hoá đơn token + tool chia số yêu cầu (274,7 đ). Giờ nhân viên chiếm 92,5% tổng chi phí; làm lại 51,8%, xem lại 40,7% [simulated].
- Theo loại [simulated]: `noi_dia` 2.696 đ (0,22× của 12.000 đ), `hang_nang` 8.221 đ (0,69×), `doi_tac` 10.215 đ (0,85×), `quoc_te` 22.515 đ (1,88×, thành công 27,3%, chạy lại không giúp). Cả hệ thống 5.865 đ/yêu cầu = 0,49× [simulated].
- Ba yếu tố nhạy nhất: số ca làm lại (+51,8%), tỉ lệ xem lại (+40,7%), lương nhân viên (+23,1%); giá token chỉ +5,6% [simulated]. Giới hạn 2 lần chạy rẻ nhất cho công ty (6.901.220 đ cả hệ thống), dù giới hạn 1 lần cho chi phí mỗi việc thấp nhất.
- Pilot: chia theo nhân viên 20 + 20; cỡ mẫu cho mức chênh 5 điểm là 1.251 mỗi nhóm nhưng cách chia này chỉ đạt tối đa 1.000, nên nhóm chấp nhận mức chênh 6 điểm (859 mỗi nhóm, power khoảng 0,64 nếu tác động thật là 5 điểm).
- **Đề xuất: Go có điều kiện** cho pilot `noi_dia` + `hang_nang`, năm điều kiện kèm người phụ trách và ngày kiểm tra (xem `ho_so_launch_v0.md`).
- Kết quả duyệt chéo từ hội đồng: (điền sau buổi duyệt chéo).

## 5. Khó khăn và cách xử lý

- Đề ghi "148 ca `chuyen_nhan_vien`" nhưng công thức so với 12.000 đ dùng 222 ca; nhóm đếm lại trong CSV và xác nhận 222 = 148 chuyển nhân viên + 74 làm lại, rồi ghi rõ khi so sánh.
- Phút làm lại trung bình lệch giữa phạm vi pilot (16,2) và toàn mẫu (15,3); nhóm dùng toàn bộ 74 ca `lam_lai` như đề và báo cáo cả hai mức hoà vốn.
- Ngưỡng an toàn tuyệt đối 3% sẽ dừng pilot ngay tuần đầu (tỉ lệ mở lại hiện tại 4,25%); nhóm đổi sang ngưỡng so với nhóm đối chứng (+2 điểm) kèm trần 6%.
- Hai ca gắn nhãn dễ lẫn giữa Hệ thống và Ngữ cảnh (16, 18); nhóm viết quy tắc phân biệt theo nguyên nhân gốc.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- Chi phí xem lại và làm lại dựa trên phút giả lập; sau tuần 1 của pilot cần thay bằng phút đo thật qua event `staff_review_decision`.
- Đợt chạy thử không có nhóm đối chứng nên không kết luận trợ lý "đã nâng" chỉ số chính (82,83% trong đợt chạy thử).
- Chia theo nhân viên không đủ mẫu cho mức chênh 5 điểm; cần thêm nhân viên, kéo dài thời gian hoặc chấp nhận mức chênh lớn hơn.
- Mô hình chi phí cộng tuyến tính, chưa mô phỏng tương tác giữa các yếu tố (ví dụ giảm xem lại có thể làm tăng lỗi lọt đến khách).
- Còn lại: loại `quoc_te` và `doi_tac` đang bị loại khỏi pilot; cần đánh giá lại khi có dữ liệu tốt hơn.

## 8. Tài liệu tham khảo

- `docs/du_lieu_va_cong_thuc.md`: dữ liệu, số liệu dùng chung và sáu công thức.
- `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` và `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`: đề bài, hướng dẫn và 20 ca lỗi.
- Google PAIR (People + AI Guidebook): năm loại lỗi dùng ở Nhiệm vụ C.
