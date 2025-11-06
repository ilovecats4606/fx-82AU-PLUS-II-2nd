# token table table for fx82au plus ii 2nd
## Manually made from realcalc
### please note that emurom tokens differ from realrom tokens slightly

> [!NOTE]
> At this point in time I am unable to find a reliable way to type the null char `00h`. If you overflow from the top, you will see it (it looks like 2 blank digits) but trying to move it out of the unstable byte will not work, it will just disappear.

| Value | Token                                                              | Char            |
| ----- | ------------------------------------------------------------------ | --------------- |
| `00h` | null                                                               |                 |
| `01h` | mᴘ                                                                 |                 |
| `02h` | mn                                                                 |                 |
| `03h` | me                                                                 |                 |
| `04h` | m𝜇                                                                 |                 |
| `05h` | ao                                                                 |                 |
| `06h` | h                                                                  |                 |
| `07h` | 𝜇ɴ                                                                 |                 |
| `08h` | 𝜇ʙ                                                                 |                 |
| `09h` | ħ                                                                  |                 |
| `0Ah` | α                                                                  |                 |
| `0Bh` | re                                                                 |                 |
| `0Ch` | 𝜆c                                                                 |                 |
| `0Dh` | γᴘ                                                                 |                 |
| `0Eh` | γcp                                                                |                 |
| `0Fh` | 𝜆cn                                                                |                 |
| `10h` | Σx²                                                                |                 |
| `11h` | Σx                                                                 |                 |
| `12h` | n                                                                  |                 |
| `13h` | Σy²                                                                |                 |
| `14h` | Σy                                                                 |                 |
| `15h` | Σxy                                                                |                 |
| `16h` | Σy³                                                                |                 |
| `17h` | ∑x²y                                                               |                 |
| `18h` | ∑x⁴                                                                |                 |
| `19h` | minX                                                               |                 |
| `1Ah` | maxX                                                               |                 |
| `1Bh` | minY                                                               |                 |
| `1Ch` | maxY                                                               |                 |
| `1Dh` | R∞                                                                 |                 |
| `1Eh` | u                                                                  |                 |
| `1Fh` | 𝜇ᴘ                                                                 |                 |
| `20h` | AtWt (there is a space after t) | _(space)_       |
| `21h` | ▯                                                                 | `!`             |
| `22h` | 𝜇e                                                                 |                 |
| `23h` | 𝜇n                                                                 |                 |
| `24h` | 𝜇𝜇 (the second one is smaller)  |                 |
| `25h` | %                                                                  | `%`             |
| `26h` | F                                                                  |                 |
| `27h` | e                                                                  |                 |
| `28h` | (                                                                  | `(`             |
| `29h` | )                                                                  | `)`             |
| `2Ah` | Nᴀ                                                                 |                 |
| `2Bh` | +                                                                  | `+`             |
| `2Ch` | ,                                                                  | `,`             |
| `2Dh` | -                                                                  | `-`             |
| `2Eh` | .                                                                  | `.`             |
| `2Fh` | .+1                                                                |                 |
| `30h` | 0                                                                  | `0`             |
| `31h` | 1                                                                  | `1`             |
| `32h` | 2                                                                  | `2`             |
| `33h` | 3                                                                  | `3`             |
| `34h` | 4                                                                  | `4`             |
| `35h` | 5                                                                  | `5`             |
| `36h` | 6                                                                  | `6`             |
| `37h` | 7                                                                  | `7`             |
| `38h` | 8                                                                  | `8`             |
| `39h` | 9                                                                  | `9`             |
| `3Ah` | :                                                                  | `:`             |
| `3Bh` | k                                                                  | `;`             |
| `3Ch` | <                                                                  | `<`             |
| `3Dh` | =                                                                  | `=`             |
| `3Eh` | >                                                                  | `>`             |
| `3Fh` | RndFix(                                                            | `?`             |
| `40h` | Vm                                                                 |                 |
| `41h` | A                                                                  | `A`             |
| `42h` | B                                                                  | `B`             |
| `43h` | C                                                                  | `C`             |
| `44h` | D                                                                  | `D`             |
| `45h` | E                                                                  | `E`             |
| `46h` | F                                                                  | `F`             |
| `47h` | ->A                                                                | `G`             |
| `48h` | ->B                                                                | `H`             |
| `49h` | ->C                                                                | `I`             |
| `4Ah` | ->D                                                                | `J`             |
| `4Bh` | ->E                                                                | `K`             |
| `4Ch` | ->F                                                                | `L`             |
| `4Dh` | ->Y                                                                | `M`             |
| `4Eh` | ×                                                                  | `N`             |
| `4Fh` | ÷                                                                  | `O`             |
| `50h` | h                                                                  | `P`             |
| `51h` | c                                                                  | `Q`             |
| `52h` | o                                                                  | `R`             |
| `53h` | b                                                                  | `S`             |
| `54h` | M                                                                  | `T`             |
| `55h` | ▶a+b𝐢                                                              | `U`             |
| `56h` | ▶r∠𝜃                                                               | `V`             |
| `57h` | !                                                                  | `W`             |
| `58h` | X                                                                  | `X`             |
| `59h` | Y                                                                  | `Y`             |
| `5Ah` | Ref(                                                               | `Z`             |
| `5Bh` | Rref(                                                              | `[`             |
| `5Ch` | ▫                                                                  |                 |
| `5Dh` | π(                                                                 | `]`             |
| `5Eh` | ^(                                                                 | `^`             |
| `5Fh` | ÷R                                                                 |                 |
| `60h` | (-) (negative, display as -)    |                 |
| `61h` | Not(                                                               | `a`             |
| `62h` | Neg(                                                               | `b`             |
| `63h` | Abs(                                                               | `c`             |
| `64h` | x̂₁                                                                 | `d`             |
| `65h` | x̂                                                                  | `e`             |
| `66h` | ŷ                                                                  | `f`             |
| `67h` | x̂₂                                                                 | `g`             |
| `68h` | log(                                                               | `h`             |
| `69h` | Σ(                                                                 | `i`             |
| `6Ah` | ∫(                                                                 | `j`             |
| `6Bh` | d/dx(                                                              | `k`             |
| `6Ch` | Pol(                                                               | `l`             |
| `6Dh` | Rec(                                                               | `m`             |
| `6Eh` | and                                                                | `n`             |
| `6Fh` | or                                                                 | `o`             |
| `70h` | sinh(                                                              | `p`             |
| `71h` | cosh(                                                              | `q`             |
| `72h` | tanh(                                                              | `r`             |
| `73h` | 𝒆^(                                                                | `s`             |
| `74h` | x10                                                                | `t`             |
| `75h` | ^2                                                                 | `u`             |
| `76h` | ^3                                                                 | `v`             |
| `77h` | ^-1                                                                | `w`             |
| `78h` | R                                                                  | `x`             |
| `79h` | c₀                                                                 | `y`             |
| `7Ah` | c₁                                                                 | `z`             |
| `7Bh` | Int(                                                               | `{`             |
| `7Ch` | @                                                                  | `\|` _(cursor)_ |
| `7Dh` | Intg(                                                              | `}`             |
| `7Eh` | xor                                                                |                 |
| `7Fh` | xnor                                                               |                 |
| `80h` | 𝐢                                                                  |                 |
| `81h` | 𝒆                                                                  |                 |
| `82h` | π                                                                  |                 |
| `83h` | ->E                                                                |                 |
| `84h` | ->F                                                                |                 |
| `85h` | °                                                                  |                 |
| `86h` | ʳ                                                                  |                 |
| `87h` | ᵍ                                                                  |                 |
| `88h` | Conjg(                                                             |                 |
| `89h` | x̄                                                                  |                 |
| `8Ah` | ȳ                                                                  |                 |
| `8Bh` | Ans                                                                |                 |
| `8Ch` | Ran#                                                               |                 |
| `8Dh` | Q1                                                                 |                 |
| `8Eh` | Q3                                                                 |                 |
| `8Fh` | med                                                                |                 |
| `90h` | sinh⁻¹(                                                            |                 |
| `91h` | cosh⁻¹(                                                            |                 |
| `92h` | tanh⁻¹(                                                            |                 |
| `93h` | 10^(                                                               |                 |
| `94h` | ≤                                                                  |                 |
| `95h` | ≠                                                                  |                 |
| `96h` | ≥                                                                  |                 |
| `97h` | ▶Simp (there is a space after t)|                 |
| `98h` | √(                                                                 |                 |
| `99h` | M+                                                                 |                 |
| `9Ah` | ᴀ                                                                  |                 |
| `9Bh` | ʙ                                                                  |                 |
| `9Ch` | ᴄ                                                                  |                 |
| `9Dh` | r                                                                  |                 |
| `9Eh` | ⋅                                                                  |                 |
| `9Fh` | ˣ√(                                                                |                 |
| `A0h` | sin(                                                               |                 |
| `A1h` | cos(                                                               |                 |
| `A2h` | tan(                                                               |                 |
| `A3h` | ln(                                                                |                 |
| `A4h` | (                                                                  |                 |
| `A5h` | ▶Conv (there is a space after v)|                 |
| `A6h` | GCD(                                                               |                 |
| `A7h` | LCM(                                                               |                 |
| `A8h` | ³√(                                                                |                 |
| `A9h` | M-                                                                 |                 |
| `AAh` | 𝜎x                                                                 |                 |
| `ABh` | sx                                                                 |                 |
| `ACh` | 𝜎y                                                                 |                 |
| `ADh` | sy                                                                 |                 |
| `AEh` | ⌟                                                                  |                 |
| `AFh` | ∠                                                                  |                 |
| `B0h` | sin⁻¹(                                                             |                 |
| `B1h` | cos⁻¹(                                                             |                 |
| `B2h` | tan⁻¹(                                                             |                 |
| `B3h` | Rnd(                                                               |                 |
| `B4h` | c₂                                                                 |                 |
| `B5h` | 𝜎                                                                  |                 |
| `B6h` | 𝜀₀                                                                 |                 |
| `B7h` | 𝜇₀                                                                 |                 |
| `B8h` | 𝗔 (for the bold chars, looks like only the left stroke is bolded)  |                 |
| `B9h` | 𝗕                                                                  |                 |
| `BAh` | 𝗖                                                                  |                 |
| `BBh` | 𝗗                                                                  |                 |
| `BCh` | 𝗘                                                                  |                 |
| `BDh` | 𝗙                                                                  |                 |
| `BEh` | 𝗣                                                                  |                 |
| `BFh` | 𝗖                                                                  |                 |
| `C0h` | det(                                                               |                 |
| `C1h` | Trn(                                                               |                 |
| `C2h` | RanInt#(                                                           |                 |
| `C3h` | arg(                                                               |                 |
| `C4h` | 𝜙₀                                                                 |                 |
| `C5h` | g                                                                  |                 |
| `C6h` | G₀                                                                 |                 |
| `C7h` | Z₀                                                                 |                 |
| `C8h` | MatA                                                               |                 |
| `C9h` | MatB                                                               |                 |
| `CAh` | MatC                                                               |                 |
| `CBh` | MatAns                                                             |                 |
| `CCh` | VctA                                                               |                 |
| `CDh` | VctB                                                               |                 |
| `CEh` | VctC                                                               |                 |
| `CFh` | VctAns                                                             |                 |
| `D0h` | P(                                                                 |                 |
| `D1h` | Q(                                                                 |                 |
| `D2h` | R(                                                                 |                 |
| `D3h` | ▶t                                                                |                 |
| `D4h` | t                                                                  |                 |
| `D5h` | G                                                                  |                 |
| `D6h` | atm                                                                |                 |
| `D7h` | in▶cm                                                             |                 |
| `D8h` | cm▶in                                                             |                 |
| `D9h` | ft▶m                                                              |                 |
| `DAh` | m▶ft                                                              |                 |
| `DBh` | yd▶m                                                              |                 |
| `DCh` | m▶yd                                                              |                 |
| `DDh` | mile▶km                                                           |                 |
| `DEh` | km▶mile                                                           |                 |
| `DFh` | n mile▶m                                                          |                 |
| `E0h` | m▶n mile                                                          |                 |
| `E1h` | acre▶m²                                                           |                 |
| `E2h` | m²▶acre                                                           |                 |
| `E3h` | gal(US)▶ℓ                                                         |                 |
| `E4h` | ℓ▶gal(US)                                                         |                 |
| `E5h` | gal(UK)▶ℓ                                                         |                 |
| `E6h` | ℓ▶gal(UK)                                                         |                 |
| `E7h` | pc▶km                                                             |                 |
| `E8h` | km▶pc                                                             |                 |
| `E9h` | km/h▶m/s                                                          |                 |
| `EAh` | m/s▶km/h                                                          |                 |
| `EBh` | oz▶g                                                              |                 |
| `ECh` | g▶oz                                                              |                 |
| `EDh` | lb▶kg                                                             |                 |
| `EEh` | kg▶lb                                                             |                 |
| `EFh` | atm▶Pa                                                            |                 |
| `F0h` | Pa▶atm                                                            |                 |
| `F1h` | mmHg▶Pa                                                           |                 |
| `F2h` | Pa▶mmHg                                                           |                 |
| `F3h` | hp▶kW                                                             |                 |
| `F4h` | kW▶hp                                                             |                 |
| `F5h` | kgf/cm²▶Pa                                                        |                 |
| `F6h` | Pa▶kgf/cm²                                                        |                 |
| `F7h` | kgf⋅m▶J                                                            |                 |
| `F8h` | J▶kgf⋅m                                                            |                 |
| `F9h` | lbf/in²▶kPa                                                       |                 |
| `FAh` | kPa▶lbf/in²                                                       |                 |
| `FBh` | °F▶°C                                                             |                 |
| `FCh` | °C▶°F                                                             |                 |
| `FDh` | J▶cal                                                             |                 |
| `FEh` | cal▶J                                                             |                 |
| `FFh` | @                                                                  |                 |
