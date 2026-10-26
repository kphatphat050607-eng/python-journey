"""Week 36 exercise: create a DienThoai class and two objects."""


class DienThoai:
    """Lưu và hiển thị thông tin của một điện thoại."""

    def __init__(
        self,
        MaMay: str,
        TenMay: str,
        HangSanXuat: str,
        DungLuongPin: int,
        GiaBan: int,
    ):
        self.MaMay = MaMay
        self.TenMay = TenMay
        self.HangSanXuat = HangSanXuat
        self.DungLuongPin = DungLuongPin
        self.GiaBan = GiaBan

    def thongtindienthoai(self) -> None:
        """In đầy đủ thông tin điện thoại."""
        print(f"Mã máy: {self.MaMay}")
        print(f"Tên máy: {self.TenMay}")
        print(f"Hãng sản xuất: {self.HangSanXuat}")
        print(f"Dung lượng pin: {self.DungLuongPin} mAh")
        print(f"Giá bán: {self.GiaBan:,} VND")
        print("-" * 35)


if __name__ == "__main__":
    dt01 = DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28990000)
    dt02 = DienThoai("DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29990000)

    dt01.thongtindienthoai()
    dt02.thongtindienthoai()
