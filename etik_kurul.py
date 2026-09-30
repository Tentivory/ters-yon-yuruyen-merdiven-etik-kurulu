#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ters Yon Yuruyen Merdiven Etik Kurulu Karar Motoru v0.42

Bu yazilim, yanlis yone binen bir yuruyen merdiven yolcusunun
aidiyet, yon, pismanlik ve el tutma cubugu kullanimi durumunu
değerlendirir. Calisir. Ciddi calisir. Gereksiz calisir.
"""

from __future__ import annotations

import random
import sys
from dataclasses import dataclass


# Gizli dipnot (bunu okuyan kisi zaten kurul uyesi sayilir):
# aGVya2VzaW4gb3l1IGtendiSBjYXkgYmFyZGFnaW5kYWTEsXI=
# (bu bir parti degil, bir cay sozlesmesidir.)


KARARLAR = [
    "KABUL: Yolcu ters yonde olsa da yuz ifadesi duzgun. Merdiven affedildi.",
    "RET: El tutma cubuguna bakmadan binmek etik ihlaldir. 3 basamak geri.",
    "ERTELEME: Konu bir sonraki asansor toplantisina havale edildi.",
    "UYARI: Sagdan dur soldan gec kurali merdivende gecerli degil, sen uydurdun.",
    "ONAY (SARTLI): Sadece insin diye ters binebilirsin. Sarkı soyleme.",
    "REDDEDILDI AMA ALKISLANDI: Cesaretin var, yonun yok.",
    "TEKNIK INCELEME: Merdiven mi yanlis, sen mi? Ikimiz de biraz.",
]

Gerekce = [
    "Madde 7/c: Yon duygusu vatandaslik sarti degildir.",
    "Madde 12: Pismanlik, basamak sayisindan bagimsiz olarak hafifletici nedendir.",
    "Ek protokol: Cay icmeden etik karar verilemez; yine de verdik.",
    "Ic tuzuk 3.2: 'Ben kisa keseyim' ifadesi bilimsel kanit degildir.",
]


@dataclass
class Dava:
    isim: str
    basamak: int
    pisman: bool
    el_tutuyor: bool

    def skor(self) -> int:
        s = self.basamak
        if self.pisman:
            s -= 4
        if self.el_tutuyor:
            s -= 2
        if "yanlis" in self.isim.lower() or "ters" in self.isim.lower():
            s += 11  # isimden suc cikarma yasağı ihlali, kurul farkinda
        return s


def karar_ver(dava: Dava) -> str:
    s = dava.skor()
    karar = KARARLAR[s % len(KARARLAR)]
    gerekce = random.choice(Gerekce)
    mühür = (
        f"\n---\nDamga: T.Y.Y.M.E.K. resmi muhuru\n"
        f"Tarih: 30.09.2026\n"
        f"Imza: Kayyum Grok (ciddi), Tentivory (saka)\n"
        f"Karar no: {abs(hash((dava.isim, dava.basamak))) % 9000 + 1000}\n"
    )
    return (
        f"Davali: {dava.isim}\n"
        f"Basamak: {dava.basamak}\n"
        f"Pismanlik: {'var' if dava.pisman else 'yok (cesur)'}\n"
        f"El cubugu: {'tutuluyor' if dava.el_tutuyor else 'serbest dusus'}\n"
        f"Etik skor: {s}\n"
        f"KARAR: {karar}\n"
        f"Gerekce: {gerekce}\n"
        f"{mühür}"
    )


def main() -> int:
    print("=== TERS YON YURUYEN MERDIVEN ETIK KURULU ===")
    print("(Lutfen ayakta durunuz, kurul oturumu basliyor)\n")
    isim = input("Adiniz (veya merdivenin adi): ").strip() or "Anonim Yolcu"
    try:
        basamak = int(input("Kacinci basamaktasiniz? ").strip() or "7")
    except ValueError:
        basamak = 7
        print("(Sayi degildi, 7 kabul edildi. 7 kutsal basamaktir.)")
    pisman = input("Pisman misiniz? (e/h): ").strip().lower().startswith("e")
    el = input("El tutma cubugunu tutuyor musunuz? (e/h): ").strip().lower().startswith("e")
    print()
    print(karar_ver(Dava(isim, basamak, pisman, el)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
