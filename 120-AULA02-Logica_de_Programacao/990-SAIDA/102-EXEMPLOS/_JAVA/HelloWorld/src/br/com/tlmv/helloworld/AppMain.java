/*
 * Copyright (c) 2025-2026 TLMV Consultoria e Sistemas EIRELI.
 * 
 * AppMain.java
 * Autor:
 * Luiz Marcio Faria de Aquino Viana, Pos-D.Sc. - Engenheiro, 28/04/2026
 * Unidade: Universidade do Estado do Rio de Janeiro
 * Curso: Engenharia Eletrica, Enfase em Engenharia de Sistemas e Computacao
 * Unico Socio e Administrador da Empresa - Desde: 02/08/2000
 * 
 * Revisoes: ...
 */

package br.com.tlmv.helloworld;

public class AppMain 
{
//Private
	
	private void procGeraValores(double[] valores) {
		int n = valores.length;
	    for(int i = 0; i < n; i++) {
	    	valores[i] = Math.random() * 1000.0;
	    }
	}

	private double funcMedia(double[] valores) {
		double soma = 0.0;

		int n = valores.length;
	    for(int i = 0; i < n; i++) {
	        double val = valores[i];
	        soma = soma + val;
	    }

	    double media = soma / (double)n;
	    return media;
	}

	private double[] funcMinMax(double[] valores) {
	    double min = 9999999.0;
	    double max = -9999999.0;

		int n = valores.length;
	    for(int i = 0; i < n; i++) {
	        double val = valores[i];

	        if(val < min)
	            min = val;

	        if(val > max)
	            max = val;
	    }
	    
	    double[] result = new double[2];
	    result[0] = min;
	    result[1] = max;
	    
	    return result;
	}

	private void procImprimeValores(double[] valores)
	{
	    System.out.print("Valores: [ ");

		int n = valores.length;
	    for(int i = 0; i < n; i++) {
	        if(i > 0)
	        	System.out.print(", ");

	        double val = valores[i];
	        System.out.print(val);
	    }
	    System.out.println(" ]\n");
	}

	private void procCopyright()
	{
		System.out.println("Copyright (c) 2025-2026 TLMV Consultoria e Sistemas EIRELI.\n");

		System.out.println("Autor: Luiz Marcio Faria de Aquino Viana, Pos-D.Sc. (COPPE/UFRJ em 2002 e 2022)");
		System.out.println("Formacao: Engenharia Eletrica com Enfase em Engenharia de Sistemas e Computacao (UERJ em 1997)");
		System.out.println("E-mail: lmarcio@tlmv.com.br - Outro e-mail: luiz.marcio.viana@gmail.com");
		System.out.println("Telefone: (21)99983-7207 - WhatsApp: (21)95911-5253\n");
	    
		System.out.println("Hello, wrold!\n");
	}
	
	/* Execute */

	public void execute()
	{
	    int n = 100;

	    double[] valores = new double[n];

	    double media;
	    double min, max;

	    this.procCopyright();
	    
	    this.procGeraValores(valores);
	    
	    media = this.funcMedia(valores);
	    
	    double[] minMax = funcMinMax(valores);
	    min = minMax[0];
	    max = minMax[1];

	    procImprimeValores(valores);

	    System.out.println("Media: " + media);
	    System.out.println("Min: " + min);
	    System.out.println("Max: " + max);
	}
	
	/* MAIN */
	
	public static void main(String[] args) {
		AppMain app = new AppMain();
		app.execute();
	}

}
