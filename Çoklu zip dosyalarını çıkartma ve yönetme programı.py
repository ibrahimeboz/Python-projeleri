import os
import zipfile
import shutil
from pathlib import Path
from datetime import datetime
#Çoklu zip dosyalarını çıkartma ve yönetme programı
oluşturan: İEB
oluşturulmatarihi: 2025-12-26

# Renkli çıktı için ANSI kodları
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    END = '\033[0m'

# İstatistik tutma
stats = {
    "total_zips": 0,
    "total_size": 0,
    "errors": 0,
    "success": 0,
    "start_time": datetime.now()
}

def get_zip_size(zip_path):
    """ZIP dosyasının boyutunu MB cinsinden döndür"""
    try:
        size_bytes = os.path.getsize(zip_path)
        return size_bytes / (1024 * 1024)  # MB'a dönüştür
    except:
        return 0

def create_backup(zip_path):
    """ZIP dosyasının yedeğini oluştur"""
    backup_path = zip_path + ".backup"
    try:
        shutil.copy2(zip_path, backup_path)
        return True
    except Exception as e:
        print(f"{Colors.RED}[!] Yedekleme başarısız ({zip_path}): {e}{Colors.END}")
        return False

def list_zip_contents(zip_path):
    """ZIP dosyasının içeriğini listele"""
    try:
        with zipfile.ZipFile(zip_path, 'r') as zf:
            file_list = zf.namelist()
            return len(file_list)
    except:
        return 0

def extract_all_zips(root_dir, backup=False, delete_after=True):
    """Tüm ZIP dosyalarını çıkart"""
    found = False
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith(".zip"):
                found = True
                zip_path = os.path.join(root, file)
                dest_folder = os.path.join(root, os.path.splitext(file)[0])
                
                zip_size = get_zip_size(zip_path)
                file_count = list_zip_contents(zip_path)
                
                stats["total_zips"] += 1
                stats["total_size"] += zip_size

                print(f"{Colors.CYAN}[>] Çıkartılıyor: {file} ({zip_size:.2f} MB, {file_count} dosya){Colors.END}")
                
                try:
                    # Yedekleme oluştur
                    if backup:
                        create_backup(zip_path)
                    
                    # ZIP'i çıkart
                    with zipfile.ZipFile(zip_path, 'r') as zf:
                        zf.extractall(dest_folder)
                    
                    stats["success"] += 1
                    
                    # ZIP'i sil
                    if delete_after:
                        os.remove(zip_path)
                        print(f"{Colors.GREEN}[✓] Başarılı ve silindi{Colors.END}")
                    else:
                        print(f"{Colors.GREEN}[✓] Başarılı{Colors.END}")
                        
                except Exception as e:
                    stats["errors"] += 1
                    print(f"{Colors.RED}[!] Hata ({file}): {e}{Colors.END}")
                    continue

    return found

def show_menu():
    """Kullanıcı menüsü göster"""
    print(f"\n{Colors.BLUE}{'='*50}{Colors.END}")
    print(f"{Colors.YELLOW}ZIP ÇIKARICI PROGRAMI - ANA MENU{Colors.END}")
    print(f"{Colors.BLUE}{'='*50}{Colors.END}")
    print("1. Tüm ZIP'leri çıkart (sil)")
    print("2. Tüm ZIP'leri çıkart (yedek + sil)")
    print("3. Tüm ZIP'leri çıkart (tutut)")
    print("4. Özel klasörü seç ve çıkart")
    print("5. İstatistikleri göster")
    print("6. Çıkış")
    print(f"{Colors.BLUE}{'='*50}{Colors.END}\n")

def show_stats():
    """İstatistikleri göster"""
    elapsed_time = (datetime.now() - stats["start_time"]).total_seconds()
    print(f"\n{Colors.CYAN}{'='*50}{Colors.END}")
    print(f"{Colors.YELLOW}İSTATİSTİKLER{Colors.END}")
    print(f"{Colors.CYAN}{'='*50}{Colors.END}")
    print(f"Toplam ZIP dosyası: {stats['total_zips']}")
    print(f"Başarılı: {stats['success']}")
    print(f"Hata: {stats['errors']}")
    print(f"Toplam boyut: {stats['total_size']:.2f} MB")
    print(f"Geçen süre: {elapsed_time:.2f} saniye")
    print(f"{Colors.CYAN}{'='*50}{Colors.END}\n")

# Ana program
if __name__ == "__main__":
    base_dir = os.getcwd()
    
    print(f"{Colors.CYAN}[*] ZIP ÇIKARICI BAŞLATILIYOR...{Colors.END}")
    print(f"{Colors.YELLOW}Klasör: {base_dir}{Colors.END}\n")
    
    while True:
        show_menu()
        choice = input(f"{Colors.YELLOW}Seçim yap (1-6): {Colors.END}").strip()
        
        if choice == "1":
            rounds = 0
            while extract_all_zips(base_dir, backup=False, delete_after=True):
                rounds += 1
                print(f"{Colors.YELLOW}[#] {rounds}. katman açıldı, devam ediliyor...{Colors.END}\n")
            print(f"{Colors.GREEN}[✓] Tüm ZIP katmanları açıldı!{Colors.END}")
            show_stats()
            
        elif choice == "2":
            rounds = 0
            while extract_all_zips(base_dir, backup=True, delete_after=True):
                rounds += 1
                print(f"{Colors.YELLOW}[#] {rounds}. katman açıldı (yedeklerle), devam ediliyor...{Colors.END}\n")
            print(f"{Colors.GREEN}[✓] Tüm ZIP katmanları açıldı! (Yedekler oluşturuldu){Colors.END}")
            show_stats()
            
        elif choice == "3":
            rounds = 0
            while extract_all_zips(base_dir, backup=False, delete_after=False):
                rounds += 1
                print(f"{Colors.YELLOW}[#] {rounds}. katman açıldı, devam ediliyor...{Colors.END}\n")
            print(f"{Colors.GREEN}[✓] Tüm ZIP katmanları açıldı! (ZIP dosyaları tutuldu){Colors.END}")
            show_stats()
            
        elif choice == "4":
            custom_dir = input(f"{Colors.YELLOW}Klasör yolunu gir: {Colors.END}").strip()
            if os.path.isdir(custom_dir):
                rounds = 0
                while extract_all_zips(custom_dir, backup=False, delete_after=True):
                    rounds += 1
                    print(f"{Colors.YELLOW}[#] {rounds}. katman açıldı, devam ediliyor...{Colors.END}\n")
                print(f"{Colors.GREEN}[✓] Özel klasördeki tüm ZIP katmanları açıldı!{Colors.END}")
                show_stats()
            else:
                print(f"{Colors.RED}[!] Klasör bulunamadı!{Colors.END}")
                
        elif choice == "5":
            show_stats()
            
        elif choice == "6":
            print(f"{Colors.GREEN}Programdan çıkılıyor...{Colors.END}")
            break
            
        else:
            print(f"{Colors.RED}[!] Geçersiz seçim!{Colors.END}")
#İEB#
