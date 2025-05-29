#pip install -U datasets huggingface_hub fsspec
import os
import json
import numpy as np
from collections import Counter
from datasets import load_dataset

# Output directory for results
output_dir = INSERT
os.makedirs(output_dir, exist_ok=True)

# List of ISO codes
languages = [
"af", "am", "ar", "az", "ca", "cy", "da", "de", "en", "es",
"et", "eu", "fa", "fr", "hi", "hr", "hu", "is", "it", "ko",
"mr", "pl", "pt", "ru", "sv", "ta", "th", "tr", "ug", "uk",
"ur", "vi"]

def ChaoWangJoost(counts):
    freqs = [c for c in counts if c > 0]
    n = float(sum(freqs))
    f1 = float(len([x for x in freqs if x == 1]))
    f2 = float(len([x for x in freqs if x == 2]))
    if f2 > 0:
        A = 2. * f2 / ((n - 1.) * f1 + 2. * f2)
    elif f1 > 0:
        A = 2. / ((n - 1.) * (f1 - 1.) + 2.)
    else:
        A = 1
    v = np.array(freqs)
    v = v[v < n]
    R = sum([(x / n) * (np.log(n) - np.log(x)) for x in v])
    r = np.arange(1, int(n))
    if A != 1.0:
        R -= f1 * (np.log(A) + sum(((1. - A) ** r) / r)) * ((1. - A) ** (1. - n)) / n
    return R

def count_phonemes_simple(phoneme_text):
    phonemes = phoneme_text.strip().split()
    return Counter(p for p in phonemes if p != "WORD_BOUNDARY")

def process_language(iso_code):
    try:
        split = "train"
        dataset = load_dataset("suchirsalhan/Phonemized-UD", iso_code)[split]

        # Entropy from word forms (based on phoneme strings)
        word_freqs = Counter()
        for example in dataset:
            text = example.get("text", "")
            words = text.split(" WORD_BOUNDARY ")
            words = [w.strip() for w in words if w.strip()]
            word_freqs.update(words)

        word_counts = np.array(list(word_freqs.values()))
        entropy = ChaoWangJoost(word_counts) if len(word_counts) > 0 else 0.0
        print(f"Language: {iso_code} | Entropy: {entropy:.4f}")

        # Phoneme-level stats
        total_phoneme_counts = Counter()
        word_strings = []

        for example in dataset:
            text = example.get("text", "")
            tokens = example.get("tokens", [])
            word_strings.extend(tokens)
            total_phoneme_counts.update(count_phonemes_simple(text))

        all_phoneme_text = '\n'.join(example.get("text", "") for example in dataset)
        words_phonemes = [w.strip().split() for w in all_phoneme_text.split("WORD_BOUNDARY") if w.strip()]
        word_lengths = [len([p for p in phonemes if p != "WORD_BOUNDARY"]) for phonemes in words_phonemes]
        mean_word_len = float(np.mean(word_lengths)) if word_lengths else 0.0

        result = {
            "lang": iso_code,
            "entropy": float(entropy),
            "mean_word_length": mean_word_len,
            "phoneme_counts": dict(total_phoneme_counts),
            "observed_phonemes_count": len(set(total_phoneme_counts.keys())),
        }

        # Save to file
        out_path = os.path.join(output_dir, f"phoneme_stats_{iso_code}.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

        print(f"Saved stats for {iso_code} to {out_path}")
        return result

    except Exception as e:
        print(f"[!] Failed for {iso_code}: {e}")
        return None

# Run for each language
for lang in languages:
    process_language(lang)
