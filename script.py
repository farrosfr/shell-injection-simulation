import os
import shlex

def vulnerable_function(user_input):
    """
    Fungsi ini rentan terhadap shell injection.
    Input dari pengguna langsung dimasukkan ke dalam perintah shell tanpa validasi.
    Ini berbahaya karena dapat memungkinkan eksekusi perintah berbahaya.
    """
    print("[INFO] Fungsi Rentan: Menjalankan perintah shell tanpa sanitasi input.")
    # Langsung mengeksekusi perintah yang menggabungkan input dari pengguna
    os.system(f"echo {user_input}")  # Jika user_input mengandung shell commands, mereka akan dieksekusi.
    
def secure_function(user_input):
    """
    Fungsi ini aman karena memvalidasi dan membersihkan input dari pengguna.
    Menggunakan fungsi shlex.quote untuk memitigasi risiko shell injection.
    """
    print("[INFO] Fungsi Aman: Menggunakan sanitasi input untuk mencegah shell injection.")
    # Memastikan input tidak mengandung karakter berbahaya
    sanitized_input = shlex.quote(user_input)  # Sanitasi input dengan shlex.quote
    os.system(f"echo {sanitized_input}")  # Hanya menjalankan perintah yang aman
    
def attempt_shell_injection():
    """
    Simulasi upaya shell injection dengan memberikan input yang berbahaya.
    Misalnya, input yang mengandung karakter ' ; rm -rf / ' yang bisa menghapus sistem.
    """
    print("\n[Simulasi] Menjalankan shell injection:")
    
    # Input berbahaya yang dimasukkan oleh pengguna
    user_input = "Hello; rm -rf /"  # Berbahaya! Ini akan mencoba menghapus sistem (jika fungsi rentan digunakan).
    
    print(f"Input pengguna yang dimasukkan: {user_input}")
    
    # Menjalankan fungsi rentan
    print("\n[Simulasi] Fungsi Rentan:")
    vulnerable_function(user_input)  # Ini akan mengeksekusi perintah berbahaya.

    # Menjalankan fungsi yang aman
    print("\n[Simulasi] Fungsi Aman:")
    secure_function(user_input)  # Ini akan mencegah eksekusi perintah berbahaya.
    
if __name__ == "__main__":
    print("[INFO] Simulasi Shell Injection")
    attempt_shell_injection()
