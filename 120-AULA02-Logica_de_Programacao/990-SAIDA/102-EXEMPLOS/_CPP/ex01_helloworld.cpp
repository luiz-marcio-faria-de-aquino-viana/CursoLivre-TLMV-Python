/*
 * Copyright (c) 2025-2026 TLMV Consultoria e Sistemas EIRELI.
 * 
 * ex01_helloworld.cpp
 * Autor:
 * Luiz Marcio Faria de Aquino Viana, Pos-D.Sc. - Engenheiro, 28/04/2026
 * Unidade: Universidade do Estado do Rio de Janeiro
 * Curso: Engenharia Eletrica, Enfase em Engenharia de Sistemas e Computacao
 * Unico Socio e Administrador da Empresa - Desde: 02/08/2000
 * 
 * Revisoes: ...
 */

#include<stdio.h>
#include<stdlib.h>
#include<time.h>

void procGeraValores(double *valores, int n) {
    time_t seed;

    localtime(& seed);
    srand(seed);

    for(int i = 0; i < n; i++) {
        long rndVal = random() % 1000000;
        valores[i] = (double)rndVal / 1000.0;
    }
}

void procMedia(double *valores, int n, double* pMedia) {
    double soma = 0.0;
    for(int i = 0; i < n; i++) {
        double val = valores[i];
        soma = soma + val;
    }

    (*pMedia) = soma / (double)n;
}

void procMinMax(double *valores, int n, double* pMin, double* pMax) {
    (*pMin) = 9999999.0;
    (*pMax) = -9999999.0;

    for(int i = 0; i < n; i++) {
        double val = valores[i];

        if(val < (*pMin))
            (*pMin) = val;

        if(val > (*pMax))
            (*pMax) = val;
    }
}

void procImprimeValores(double* valores, int n)
{
    printf("Valores: [ ");

    for(int i = 0; i < n; i++) {
        if(i > 0)
            printf(", ");

        double val = valores[i];
        printf("%lf", val);
    }
    printf(" ]\n\n");
}

void procCopyright()
{
    printf("Copyright (c) 2025-2026 TLMV Consultoria e Sistemas EIRELI.\n\n");

    printf("Autor: Luiz Marcio Faria de Aquino Viana, Pos-D.Sc. (COPPE/UFRJ em 2002 e 2022)\n");
    printf("Formacao: Engenharia Eletrica com Enfase em Engenharia de Sistemas e Computacao (UERJ em 1997)\n");
    printf("E-mail: lmarcio@tlmv.com.br - Outro e-mail: luiz.marcio.viana@gmail.com\n");
    printf("Telefone: (21)99983-7207 - WhatsApp: (21)95911-5253\n\n");
    
    printf("Hello, wrold!\n\n");
}

int main(int argc, char** argv)
{
    int n = 10000;

    double valores[n];

    double media;
    double min, max;

    procCopyright();
    procGeraValores(valores, n);
    procMedia(valores, n, & media);
    procMinMax(valores, n, & min, & max);

    procImprimeValores(valores, n);

    printf("Media: %lf\n\n", media);
    printf("Min: %lf\n", min);
    printf("Max: %lf\n", max);

    return(0);
}
