import ROOT as R
import sys
if __name__ == '__main__':
	f_r21a = R.TFile.Open("/user/zhiyuan/Code/RUA/source/MIA/data/FF_by_Jordan.root", "read")
	f_r21d = R.TFile.Open("/user/zhiyuan/Code/RUA/run/fftest/FF_by_Jordan_updated.root", "read")
	f_r21combined = R.TFile.Open("/user/zhiyuan/Code/RUA/run/fftest/FF_by_Jordan_combined.root", "read")
	f_r207a = R.TFile.Open("/user/zhiyuan/Code/RUA/source/MIA/data/FF.data.root", "read")
	# f_r21combined = R.TFile.Open("/user/gwilliam/NtupleAnalysis/ATLASRunII_r21/run/Fakes/FF.data.root", "read")
	# f_r21combined = R.TFile.Open("/user/zhiyuan/Code/RUA/source/MIA/data/FF.data.root")







	canvas = {}
	hist_r21a = {}
	hist_r21d = {}
	hist_r21combined = {}
	hist_r207a = {}
	legend = {}


	x = 0.15
	y = 0.8
	text = "Work in progress"

	#delx = 0.115*696*R.gPad.GetWh()/(472*R.gPad.GetWw())


	# don't use continue, it goes back to the top of iteration
	for region in ['CR', 'CR_SS', 'HighMtCR', 'HighMtCR_SS']:
		for cut in ['Preselection', 'HighMTW']:
			for Ntag in ['0','1','2']:
				for Np in ['Np1', 'Np3']:
					name = region+cut+Ntag+Np
					path = "/".join([region, "All", cut, Np, "Nb"+Ntag, 'TauPt'])
					#path_40 = "/".join([region, "All", cut, Np, "Nb"+Ntag, 'TauPt40'])

					canvas[name] = R.TCanvas(name, "atlas", 0,0,800,600)
					canvas[name].cd()

					legend[name] = R.TLegend(0.7,0.65,0.98,0.93)
					#legend[name] = R.TLegend(0.2,0.7,0.4,0.85)
					legend[name].SetTextSize(0.04)
					
					R.gStyle.SetOptStat(0)
					try:
						hist_r21a[name] = f_r21a.Get(path)
						if "CR" in region:
						 	if "SS" in region:
						 		if Np == 'Np1':
						 			hist_r21a[name].SetTitle("#font[52]"+"{" +",".join(["FF", "InvIso SS region", "1 prong", Ntag+" tag"]) +"}")
						 		else:
						 			hist_r21a[name].SetTitle("#font[52]"+"{" +",".join(["FF", "InvIso SS region", "3 prong", Ntag+" tag"]) +"}")
						 	else: 
						 		if Np == 'Np1':
						 			hist_r21a[name].SetTitle("#font[52]"+"{" +",".join(["FF","InvIso region",  "1 prong", Ntag+" tag"]) +"}")
						 		else:
						 			hist_r21a[name].SetTitle("#font[52]"+"{" +",".join(["FF","InvIso region",  "3 prong", Ntag+" tag"]) +"}")
						else: 
						 	if "SS" in region:
						 		if Np == 'Np1':
						 			hist_r21a[name].SetTitle("#font[52]"+"{" +",".join(["FF", "HighMTW SS region", "1 prong", Ntag+" tag"]) +"}")
						 		else:
						 			hist_r21a[name].SetTitle("#font[52]"+"{" +",".join(["FF", "HighMTW SS region", "3 prong", Ntag+" tag"]) +"}")
						 	else: 
						 		if Np == 'Np1':
						 			hist_r21a[name].SetTitle("#font[52]"+"{" +",".join(["FF","HighMTW region",  "1 prong", Ntag+" tag"]) +"}")
						 		else:
						 			hist_r21a[name].SetTitle("#font[52]"+"{" +",".join(["FF","HighMTW region",  "3 prong", Ntag+" tag"]) +"}")

						hist_r21a[name].GetYaxis().SetTitle("#font[52]{Fake factor}")
						hist_r21a[name].GetYaxis().SetTitleOffset(1.2)
						hist_r21a[name].GetYaxis().SetRangeUser(0,0.5)
						hist_r21a[name].GetXaxis().SetTitle("#font[52]{#tau p_{T}}[GeV]")
						print(path)
						hist_r21a[name].Draw('same')

						
					except ReferenceError:
						pass
					except AttributeError: 
						pass
					# try: 	
					# 	hist_r21d[name] = f_r21d.Get(path_40)
					# 	hist_r21d[name].SetTitle(path_40)
					# 	hist_r21d[name].Draw("same")
					# 	hist_r21d[name].SetMarkerColor(2)
					# 	hist_r21d[name].SetLineColor(2)
					# 	legend[name].AddEntry(hist_r21d[name], "r21 mc16d", "l")
					# except ReferenceError:
					# 	pass
					# except AttributeError: 
					# 	pass

					try: 	
						hist_r21d[name] = f_r21d.Get(path)
						hist_r21d[name].Draw("same")
						hist_r21d[name].SetMarkerColor(2)
						hist_r21d[name].SetLineColor(2)
						
					except ReferenceError:
						pass
					except AttributeError: 
						pass
					
					try:
						hist_r21combined[name] = f_r21combined.Get(path)
						hist_r21combined[name].Draw("same")
						hist_r21combined[name].SetMarkerColor(3)
						hist_r21combined[name].SetLineColor(3)
						
					except ReferenceError:
						pass
					except AttributeError: 
						pass
					# try: 	
					# 	hist_r21combined[name] = f_r21combined.Get(path_40)
					# 	hist_r21combined[name].SetTitle(path_40)
					# 	hist_r21combined[name].Draw("same")
					# 	hist_r21combined[name].SetMarkerColor(3)
					# 	hist_r21combined[name].SetLineColor(3)
					# 	legend[name].AddEntry(hist_r21combined[name], "r20.7 mc16a", "l")	
					# except: 
					# 	pass
					try:
						hist_r207a[name] = f_r207a.Get(path)
						hist_r207a[name].Draw("same")
						hist_r207a[name].SetMarkerColor(4)
						hist_r207a[name].SetLineColor(4)
						
					except ReferenceError:
						pass
					except AttributeError: 
						pass					
					legend[name].AddEntry(hist_r207a[name], "#font[52]{r20.7 mc16a FF}", "l")
					legend[name].AddEntry(hist_r21a[name], "#font[52]{r21 mc16a FF}", "l")
					legend[name].AddEntry(hist_r21d[name], "#font[52]{r21 mc16d FF}", "l")
					legend[name].AddEntry(hist_r21combined[name], "#font[52]{r21 combined FF}", "l")
					legend[name].Draw("same")



					l = R.TLatex()
					l.SetNDC()
					l.SetTextFont(72)
	
					p = R.TLatex()
					p.SetNDC()
					p.SetTextFont(42)
				
					l.DrawLatex(x,y,"ATLAS")
					p.DrawLatex(x+0.13,y,text)

					canvas[name].Update()
					canvas[name].Print("_".join([region, "All", cut, Np, "Nb"+Ntag, 'TauPt']) + '.png')
					



	for region in ['rQCD_CR', 'rQCD_CR_SS']:
		for cut in ['Preselection']:
			for lep in ['Elec', 'Muon']:
				for Ntag in ['0','1','2']:
					for Np in ['Np1', 'Np3']:
						name = region+cut+Ntag+Np+lep
						legend[name] = R.TLegend(0.7,0.65,0.98,0.93)
						canvas[name] = R.TCanvas(name, "atlas", 0,0,800,600)
						canvas[name].cd()
						R.gStyle.SetOptStat(0)

					 	hist_r21d[name] = f_r21d.Get("/".join([region, "All", cut, lep, Np, "Nb"+Ntag, 'TauPt']))

					 	if region == "rQCD_CR_SS":
					 		if Np == 'Np1':
					 			hist_r21d[name].SetTitle("#font[52]"+"{" +",".join(["rQCD", "SS region", cut, lep + " channel",  "1 prong", Ntag+" tag"]) +"}")
					 		else:
					 			hist_r21d[name].SetTitle("#font[52]"+"{" +",".join(["rQCD", "SS region", cut, lep + " channel",  "3 prong", Ntag+" tag"]) +"}")
					 	else: 
					 		if Np == 'Np1':
					 			hist_r21d[name].SetTitle("#font[52]"+"{" +",".join(["rQCD",cut, lep + " channel",  "1 prong", Ntag+" tag"]) +"}")
					 		else:
					 			hist_r21d[name].SetTitle("#font[52]"+"{" +",".join(["rQCD",cut, lep + " channel",  "3 prong", Ntag+" tag"]) +"}")
						hist_r21d[name].GetYaxis().SetTitle("#font[52]{rQCD}")
						hist_r21d[name].GetYaxis().SetTitleOffset(1.3)
						hist_r21d[name].GetXaxis().SetTitle("#font[52]{#tau p_{T}}[GeV]")
						hist_r21d[name].Draw("same")
						hist_r21d[name].SetLineColor(2)
						hist_r21d[name].SetMarkerColor(2)
						
						hist_r21d[name].GetYaxis().SetRangeUser(0,0.5)
							
							
						hist_r21a[name] = f_r21a.Get("/".join([region, "All", cut, lep, Np, "Nb"+Ntag, 'TauPt']))
						hist_r21a[name].Draw('same')
						
					
						#print('no r21as histogram: ' + "/".join([region, "All", cut, lep, Np, "Nb"+Ntag, 'TauPt']))

						
						
						
						#print('no r21d histogram: ' + "/".join([region, "All", cut, lep, Np, "Nb"+Ntag, 'TauPt']))	

						
						hist_r21combined[name] = f_r21combined.Get("/".join([region, "All", cut, lep, Np, "Nb"+Ntag, 'TauPt']))
						hist_r21combined[name].Draw("same")
						hist_r21combined[name].SetLineColor(3)
						hist_r21combined[name].SetMarkerColor(3)
						


						hist_r207a[name] = f_r207a.Get("/".join([region, "All", cut, lep, Np, "Nb"+Ntag, 'TauPt']))
						hist_r207a[name].Draw("same")
						hist_r207a[name].SetLineColor(4)
						hist_r207a[name].SetMarkerColor(4)
						
					
						#print('no r21combined histogram: ' + "/".join([region, "All", cut, lep, Np, "Nb"+Ntag, 'TauPt']))	
						legend[name].AddEntry(hist_r207a[name], "#font[52]{r20.7 mc16a rQCD}", "l")
						legend[name].AddEntry(hist_r21a[name], "#font[52]{r21 mc16a rQCD}", "l")
						legend[name].AddEntry(hist_r21d[name], "#font[52]{r21 mc16d rQCD}", "l")
						legend[name].AddEntry(hist_r21combined[name], "#font[52]{r21 combined rQCD}", "l")
						
						legend[name].Draw("same")



						l = R.TLatex()
						l.SetNDC()
						l.SetTextFont(72)
		
						p = R.TLatex()
						p.SetNDC()
						p.SetTextFont(42)
					
						l.DrawLatex(x,y,"ATLAS")
						p.DrawLatex(x+0.13,y,text)




						canvas[name].Update()
						canvas[name].Print("_".join([region, "All", cut, lep, Np, "Nb"+Ntag, 'TauPt']) + '.png')


						

						# ff_c.cd(int(Ntag) + 1)
						# hist[name + Ntag + Np].SetTitle(name + Ntag + 'tag' + '1/3' + 'prong')
						# hist[name + Ntag + Np].SetLineColor(color)
						# hist[name + Ntag + Np].SetMarkerColor(color)
						# hist[name + Ntag + Np].Draw('e,same')
						# hist[name + Ntag + Np].GetYaxis().SetRangeUser(0 , 0.5)
						# leg[name + Ntag].AddEntry(hist[name + Ntag + Np], Np, "L");
						# leg[name + Ntag].Draw('same')
						# color += 1
						# ff_c.Update()
	f_r21a.Close()
	f_r21d.Close()
	f_r21combined.Close()