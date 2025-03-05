from collections import deque

def cari_kata_dengan_BFS(matriks, kata):
    baris = len(matriks)
    kolom = len(matriks[0])
    arah = [(0,1), (1,0)]  # Bisa ke kanan atau ke bawah

    # Cari semua posisi awal dari huruf pertama dalam kata
    for i in range(baris):
        for j in range(kolom):
            if matriks[i][j] == kata[0]:
                antrian = deque([(i, j, 0)])  # (x, y, indeks huruf saat ini)
                dikunjungi = {(i, j)}

                # Lakukan BFS
                while antrian:
                    x, y, idx = antrian.popleft()

                    # Jika sudah menemukan semua huruf dalam kata
                    if idx == len(kata) - 1:
                        return True  

                    for dx, dy in arah:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < baris and 0 <= ny < kolom and (nx, ny) not in dikunjungi:
                            if matriks[nx][ny] == kata[idx + 1]:
                                antrian.append((nx, ny, idx + 1))
                                dikunjungi.add((nx, ny))

    return False  # Kata tidak ditemukan

# Contoh penggunaan
matriks = [
    ['C', 'A', 'T'],
    ['X', 'T', 'A'],
    ['Y', 'Z', 'T']
]
kata = "CAT"

hasil = cari_kata_dengan_BFS(matriks, kata)
if hasil:
    print("Kata", kata, "ditemukan dalam matriks.")
else:
    print("Kata", kata, "tidak ditemukan dalam matriks.")