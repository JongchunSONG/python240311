from openpyxl import Workbook
import random

# 제품 정보 생성
def generate_product_data():
    products = []
    for i in range(100):
        product_id = i + 1
        product_name = f"제품{product_id}"
        product_price = random.randint(1000, 10000)  # 임의의 가격 생성 (1000원에서 10000원 사이)
        products.append((product_id, product_name, product_price))
    return products

# 제품 정보를 엑셀 파일에 저장
def save_product_data(products):
    wb = Workbook()
    ws = wb.active
    ws.append(["제품ID", "제품이름", "제품가격"])
    for product in products:
        ws.append(product)
    wb.save("전자제품_데이터.xlsx")

if __name__ == "__main__":
    products = generate_product_data()
    save_product_data(products)
    print("데이터가 성공적으로 생성되고 엑셀 파일에 저장되었습니다.")
