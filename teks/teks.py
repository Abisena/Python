import string
from collections import Counter

def clean_text(text):
    # Menghapus tanda baca dan mengubah teks menjadi huruf kecil
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator).lower()
    return cleaned_text

def analyze_text(text):
    cleaned_text = clean_text(text)
    words = cleaned_text.split()
    word_count = Counter(words)

    print("Teks asli:")
    print(text)
    print("\nHasil analisis:")
    print("Jumlah kata:", len(words))
    print("Kata-kata unik:", len(word_count))
    print("\nFrekuensi kemunculan kata:")
    for word, count in word_count.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    sample_text = """
    Ini adalah contoh teks untuk analisis.
    Teks ini akan dibagi menjadi kata-kata
    dan frekuensi kemunculan setiap kata akan dihitung.
    """

    analyze_text(sample_text)
