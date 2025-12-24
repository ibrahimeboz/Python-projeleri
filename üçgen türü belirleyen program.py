"""
Üç kenarı verilen bir üçgenin türünü belirleyen program.
- Girdi doğrulama (pozitif sayılar)
- Ondalık ayırıcı olarak ',' veya '.' kabul eder
- Eşitlik için tolerans kullanır (float hassasiyeti)
- Komut satırı argümanları ile çalışabilir: python üçgen türü belirleyen program.py 3 4 5
- Çalışma modunda kullanıcı 'q' ile çıkabilir
"""

import sys

REL_TOL = 1e-9
ABS_TOL = 1e-12

def parse_number(s: str) -> float:
    s = s.strip().replace(",", ".")
    return float(s)

def are_equal(x: float, y: float, rel_tol: float = REL_TOL, abs_tol: float = ABS_TOL) -> bool:
    return abs(x - y) <= max(rel_tol * max(abs(x), abs(y)), abs_tol)

def is_valid_triangle(a: float, b: float, c: float) -> bool:
    return a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a)

def triangle_type(a: float, b: float, c: float) -> str:
    if are_equal(a, b) and are_equal(b, c):
        return "EŞKENAR"
    if are_equal(a, b) or are_equal(a, c) or are_equal(b, c):
        return "İKİZKENAR"
    return "ÇEŞİTKENAR"

def handle_three_values(a: float, b: float, c: float) -> None:
    if not is_valid_triangle(a, b, c):
        print("Bu kenarlarla üçgen oluşturulamaz.")
        return
    print(f"Bu bir {triangle_type(a, b, c)} üçgendir.")

def interactive_loop() -> None:
    print("Üçgen türü belirleyici. Ondalık için '.' veya ',' kullanın. Çıkmak için 'q' yazın.")
    while True:
        try:
            s = input("1. kenarı girin (çıkmak için q): ").strip()
            if s.lower() == "q":
                print("Çıkılıyor.")
                break
            a = parse_number(s)

            s = input("2. kenarı girin (çıkmak için q): ").strip()
            if s.lower() == "q":
                print("Çıkılıyor.")
                break
            b = parse_number(s)

            s = input("3. kenarı girin (çıkmak için q): ").strip()
            if s.lower() == "q":
                print("Çıkılıyor.")
                break
            c = parse_number(s)

            handle_three_values(a, b, c)
        except ValueError:
            print("Geçersiz sayı. Lütfen tekrar deneyin.")

def main(argv):
    if len(argv) >= 4:
        try:
            a = parse_number(argv[1])
            b = parse_number(argv[2])
            c = parse_number(argv[3])
            handle_three_values(a, b, c)
            return
        except ValueError:
            print("Komut satırı argümanlarında geçersiz sayı. İnteraktif moda geçiliyor.")
    interactive_loop()

if __name__ == "__main__":
    main(sys.argv)
