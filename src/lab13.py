"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if k is None:
        return 1 / p
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return 1.0
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:  # dùng cho B1, B3
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()
    return dict(token=tien_token.sum(), tool=tien_tool.sum(),
                chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong,
                hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs))


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')
    # TODO CP1 · Nhiệm vụ A3: tính lại theo từng giá trị của cột loai.
    # ---------- Nhiệm vụ A3 · Tách theo loại yêu cầu ----------
    print('\nA3 · Theo loại yêu cầu [simulated]')
    print(f'{"loai":10s} {"so_yc":>6s} {"ti_le_tc":>9s} {"lan/yc":>7s} {"cps":>8s} {"so_voi_12k":>10s}')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        rq = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, rq)
        n_runs = runs['request_id'].isin(rq['request_id']).sum()
        print(f'{loai:10s} {len(rq):6d} {kq["thanh_cong"] / len(rq):9.1%} '
              f'{n_runs / len(rq):7.2f} {kq["cps"]:8,.0f} {kq["cps"] / BASELINE:9.2f}x')
    # Chạy lại có giúp không: tỉ lệ ok theo từng lần thử
    mg = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    mg['ok'] = (mg['status'] == 'ok').astype(float)
    print('\nTỉ lệ ok theo lần thử (attempt):')
    print(mg.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean').round(3))
    # ---------- Nhiệm vụ A4 · Chi phí cố định (phạm vi noi_dia + hang_nang) ----------
    CO_DINH_THANG = 40_000_000   # đồng / tháng
    YC_THANG = 45_000            # yêu cầu / tháng ở quy mô đầy đủ
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kv = mo_hinh(runs, pham_vi)
    print('\nA4 · Chi phí cố định, phạm vi noi_dia + hang_nang [simulated]')
    print(f'Chi phí mỗi việc thành công trong phạm vi: {kv["cps"]:,.0f} đ ({kv["thanh_cong"]} việc)')
    for ten, yc in [('45.000 yc/tháng', YC_THANG), ('Một nửa khối lượng', YC_THANG / 2)]:
        viec_thang = yc * kv['thanh_cong'] / len(reqs)
        cd = CO_DINH_THANG / viec_thang
        print(f'{ten:20s} việc/tháng {viec_thang:8,.0f}  cố định/việc {cd:6,.0f}  '
              f'tổng {kv["cps"] + cd:6,.0f} đ = {(kv["cps"] + cd) / BASELINE:.2f}x')
    # TODO CP2 · Nhiệm vụ B: đổi từng yếu tố, ghi vào bảng độ nhạy.
    # ---------- B1 · Đổi từng yếu tố ----------
    kich_ban = {
        'Giá token gấp đôi':        dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa':   dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi':          dict(he_so_xem_lai=2),
        'Xem lại giảm một nửa':     dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi':          dict(he_so_lam_lai=2),
        'Làm lại giảm một nửa':     dict(he_so_lam_lai=0.5),
        'Lương tăng 25%':           dict(luong_phut=2500),
        'Tối đa 2 lần chạy':        dict(max_lan_chay=2),
        'Chỉ 1 lần chạy':           dict(max_lan_chay=1),
    }
    goc = mo_hinh(runs, reqs)['cps']
    print('\nB1 · Độ nhạy [simulated]')
    print(f'{"Gốc (A2)":25s} {goc:8,.0f}')
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        print(f'{ten:25s} {cps:8,.0f} {(cps / goc - 1) * 100:+6.1f}%')

    # ---------- B2 · Đổi một cặp và xếp hạng ----------
    cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    print(f'\nB2 · Giá token x2 + xem lại x2: {cap:,.0f} đ ({(cap / goc - 1) * 100:+.1f}%)')

    # ---------- B3 · Giới hạn chạy lại có thật sự rẻ hơn ----------
    print('\nB3 · Giới hạn chạy lại [simulated]')
    print(f'{"Giới hạn":9s} {"Tổng trợ lý":>12s} {"Không TC":>9s} {"Cả hệ thống":>12s} {"CPS":>7s}')
    for gh in (1, 2, 3):
        m = mo_hinh(runs, reqs, max_lan_chay=gh)
        khong_tc = len(reqs) - m['thanh_cong']
        he_thong = m['tong'] + BASELINE * khong_tc
        print(f'{gh:>3d} lần   {m["tong"]:12,.0f} {khong_tc:9d} {he_thong:12,.0f} {m["cps"]:7,.0f}')

    # ---------- B4 · Nếu phải xem lại tất cả (noi_dia + hang_nang) ----------
    pv = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    runs_pv = runs[runs['request_id'].isin(pv['request_id'])]
    token_tool = (runs_pv['tokens_in'] / 1000 * GIA_VAO + runs_pv['tokens_out'] / 1000 * GIA_RA
                  + runs_pv['tool_calls'] * GIA_TOOL).sum()
    n_xem = runs_pv.loc[runs_pv['status'] == 'ok', 'request_id'].nunique()   # có ít nhất 1 lần ok
    n_lam_lai = (pv['ket_qua'] == 'lam_lai').sum()
    n_tc = (pv['ket_qua'] == 'thanh_cong').sum()
    # trung bình trên TOÀN BỘ ca lam_lai của mẫu (74 ca), không chỉ phạm vi pilot
    phut_ll_tb = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    print(f'\nB4 · Xem lại 100% (noi_dia + hang_nang) [simulated]: {n_xem} yc xem lại, '
          f'{n_lam_lai} ca làm lại, {n_tc} việc thành công, token+tool {token_tool:,.0f} đ')
    for nhan, phut_ll in [('đề cho 9 phút/ca', 9), (f'dữ liệu {phut_ll_tb:.1f} phút/ca', phut_ll_tb)]:
        tong = n_xem * 5 * LUONG_PHUT + n_lam_lai * phut_ll * LUONG_PHUT + token_tool
        hoa_von = (BASELINE * n_tc - token_tool - n_lam_lai * phut_ll * LUONG_PHUT) / (n_xem * LUONG_PHUT)
        print(f'  Làm lại {nhan:22s}: tổng {tong:,.0f} đ -> {tong / n_tc:,.0f} đ/việc = '
              f'{tong / n_tc / BASELINE:.2f}x; hoà vốn xem lại <= {hoa_von:.1f} phút')
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
    # ---------- D1 · Cỡ mẫu theo các cách chia ----------
    from statistics import NormalDist
    from statsmodels.stats.proportion import proportion_effectsize
    from statsmodels.stats.power import NormalIndPower

    def co_mau(p1, p2, alpha=0.05, power=0.8):
        za, zb = NormalDist().inv_cdf(1 - alpha / 2), NormalDist().inv_cdf(power)
        pb = (p1 + p2) / 2
        return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                          + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)

    ICC = 0.02
    n_a = co_mau(0.70, 0.75)
    print(f'\nD1 · a) Chia theo yêu cầu: {n_a:,} yêu cầu mỗi nhóm')
    de_b = 1 + (75 - 1) * ICC
    n_b = math.ceil(n_a * de_b)
    nv_b = math.ceil(n_b / 75)
    print(f'D1 · b) m=75: DE={de_b:.2f}, n={n_b:,.0f} mỗi nhóm, {nv_b} người mỗi nhóm, '
          f'tổng {2 * nv_b} so với 40 nhân viên -> {"đủ" if 2 * nv_b <= 40 else "KHÔNG đủ người"}')
    print(f'D1 · c) 20 nhân viên mỗi nhóm: tối đa {20 / ICC:,.0f} < {n_a:,} -> '
          f'{"đạt" if 20 / ICC >= n_a else "KHÔNG đạt"}')
    print(f'D1 · d) 6 depot mỗi nhóm: tối đa {6 / ICC:,.0f}')
    n6 = co_mau(0.70, 0.76)
    m_e = math.ceil(n6 * (1 - ICC) / (20 - n6 * ICC))   # 20m/(1+(m-1)ICC) >= n6
    print(f'D1 · e) Mức chênh 6 điểm: {n6} mỗi nhóm; 20 người mỗi nhóm cần m >= {m_e} yêu cầu/người '
          f'(DE={1 + (m_e - 1) * ICC:.2f})')
    pw = NormalIndPower().power(proportion_effectsize(0.75, 0.70), nobs1=n6 / 1, alpha=0.05)
    print(f'D1 · power khi chỉ chạy {n6} mỗi nhóm mà tác động thật là 5 điểm: {pw:.2f}')
    # D3 · tỉ lệ mở lại hiện tại, để chốt ngưỡng an toàn
    pv_ = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    print(f'D3 · mo_lai_trong_7_ngay: toàn mẫu {reqs.mo_lai_trong_7_ngay.mean():.2%} '
          f'({reqs.mo_lai_trong_7_ngay.sum()}/{len(reqs)}), noi_dia+hang_nang {pv_.mo_lai_trong_7_ngay.mean():.2%}')
