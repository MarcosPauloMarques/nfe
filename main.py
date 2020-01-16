
import pdfkit
import xml.etree.ElementTree as ET

arquivo = "danfe.xml"
arquivo_xml = """
<?xml version="1.0"?>
<catalog>
   <product description="Cardigan Sweater" product_image="cardigan.jpg">
      <catalog_item gender="Men's">
         <item_number>QWZ5671</item_number>
         <price>39.95</price>
         <size description="Medium">
            <color_swatch image="red_cardigan.jpg">Red</color_swatch>
            <color_swatch image="burgundy_cardigan.jpg">Burgundy</color_swatch>
         </size>
         <size description="Large">
            <color_swatch image="red_cardigan.jpg">Red</color_swatch>
            <color_swatch image="burgundy_cardigan.jpg">Burgundy</color_swatch>
         </size>
      </catalog_item>
      <catalog_item gender="Women's">
         <item_number>RRX9856</item_number>
         <price>42.50</price>
         <size description="Small">
            <color_swatch image="red_cardigan.jpg">Red</color_swatch>
            <color_swatch image="navy_cardigan.jpg">Navy</color_swatch>
            <color_swatch image="burgundy_cardigan.jpg">Burgundy</color_swatch>
         </size>
         <size description="Medium">
            <color_swatch image="red_cardigan.jpg">Red</color_swatch>
            <color_swatch image="navy_cardigan.jpg">Navy</color_swatch>
            <color_swatch image="burgundy_cardigan.jpg">Burgundy</color_swatch>
            <color_swatch image="black_cardigan_medium.jpg">Black</color_swatch>
         </size>
         <size description="Large">
            <color_swatch image="navy_cardigan.jpg">Navy</color_swatch>
            <color_swatch image="black_cardigan_large.jpg">Black</color_swatch>
         </size>
         <size description="Extra Large">
            <color_swatch image="burgundy_cardigan.jpg">Burgundy</color_swatch>
            <color_swatch image="black_cardigan_xlarge.jpg">Black</color_swatch>
         </size>
      </catalog_item>
   </product>
</catalog>
"""

tree = ET.parse(arquivo)
root= tree.getroot()

thisdict={}

for i in range(0,len(root[0])):
    for j, texto in enumerate(root[0][i]):
        print("{}: {}".format(texto.tag.replace("{http://www.portalfiscal.inf.br/nfe}",""),texto.text))
        thisdict[(texto.tag.replace("{http://www.portalfiscal.inf.br/nfe}",""))] = texto.text

chaveAcesso= 35200130070683000114550010000257141001075108
inputString = """ 





"""

#pdfkit.from_string(inputString,'output.pdf')
