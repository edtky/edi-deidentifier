# EDI De-Identifier

De-identify your EDI-835 using this local python program.

Example Input:  
```
~N1*PR*UNITED HEALTHCARE INSURANCE COMPANY*XV*87726  
~N3*9900 BREN ROAD  
~N4*MINNETONKA*MN*553439664  
~REF*2U*87726  
~PER*CX*UNITEDHEALTHCARE SERVICES INC AND ITS AFFILIATES*TE*8778423210  
~PER*BL**UR*WWW.UNITEDHEALTHCAREONLINE.COM/B2C/CONTACTUS.DO  
~N1*PE*KLAUS MEDICAL CENTER*XX*1922164458  
~N3*NORTH POLE  
~N4*NORTH POLE*NP*00000  
```

Example Output:  
```
~N1*PR*EXAMPLE INSURANCE COMPANY*XV*88888
~N3*123 MAIN ST
~N4*SAN FRANCISCO*CA*94321
~REF*2U*87726
~PER*CX*EXAMPLE SERVICES*TE*8001119999
~PER*BL**UR*WWW.EXAMPLE.ORG
~N1*PE*EXAMPLE MEDICAL CENTER*XX*1234567890
~N3*123 MAIN ST
~N4*SAN FRANCISCO*CA*94321
```

# Quick Use ⚡️

1. Clone repo to your destop
    ```bash
    git clone https://github.com/edtky/edi-deidentifier.git
    ```

2. Copy and paste your EDI 835 file into the `input` folder (or try our sample files)

3. Run the python script to perform the deidentification.
    ```bash
    python run.py <YOUR_INPUT_835_FILE>
    ```

4. Find the de-identified file in the `output` folder