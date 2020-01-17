from nfelib.v4_00 import leiauteNFe_sub as parser
from nfelib.v4_00 import leiauteNFe as leiauteNFe4
import pdfkit
import sys
import code128
import barcode
import base64
import os

arquivo = "35191059105833000160550010000794031558766976.xml"

nota = parser.parse(arquivo)
# print(nota.infNFe.ide.cNF)

x = nota.infNFe
# print(nota.infNFe.transp.vol.Vol)

codAcesso = x.Id.replace("NFe", "")

listProduto = []

class Produto:
    cPro = 0
    xProd = ''
    NCM = 0
    CEST = 0
    CFOP = 0
    uCom = ''
    qCom = 0
    vUnCom = 0
    vProd = 0

for item in iter(x.det):
    #listProduto.clear()
    p = Produto()
    p.cPro = item.prod.cProd
    p.xProd = item.prod.xProd
    p.NCM = item.prod.NCM
    p.CEST = item.prod.CEST
    p.CFOP = item.prod.CFOP
    p.uCom = item.prod.uCom
    p.qCom = item.prod.qCom
    p.vUnCom = item.prod.vUnCom
    p.vProd = item.prod.vProd
    listProduto.append(p)

texto = ""
texto2 =""

for item in listProduto:
    if(item.CEST == None):
        item.CEST = 0
    texto += str("<tr>" + "<td>" + str(item.cPro) + "</td>" + "<td>" + str(item.xProd) + "</td>" + "<td>" + str(item.NCM) + "</td>" + "<td>" + str(item.CEST) + "</td>" + "<td>" + str(item.CFOP) + "</td>" + "<td>" + str(item.uCom) + "</td>" + "<td>" + str(item.qCom) + "</td>" + "<td>" + str(item.vUnCom) + "</td>" + "<td>" + str(item.vProd) + "</td>" + "</tr>")

EAN = barcode.get_barcode_class('code128')
ean = EAN(codAcesso)
fullname = ean.save(codAcesso,text='')

with open(fullname, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())

encoded_string = encoded_string.decode('utf-8')

input_string_css = """
 <style type="text/css">
    @media print {
        @page {
            margin-left: 15mm;
            margin-right: 15mm;
        }

        footer {
            page-break-after: always;
        }
    }

    * {
        margin: 0;
    }

    .ui-widget-content {
        border: none !important;
    }

    .nfe-square {
        margin: 0 auto 2cm;
        box-sizing: border-box;
        width: 2cm;
        height: 1cm;
        border: 1px solid #000;
    }

    .nfeArea.page {
        width: 18cm;
        position: relative;
        font-family: "Times New Roman", serif;
        color: #000;
        margin: 0 auto;
        overflow: hidden;
    }

    .nfeArea .font-12 {
        font-size: 12pt;
    }

    .nfeArea .font-8 {
        font-size: 8pt;
    }

    .nfeArea .bold {
        font-weight: bold;
    }

    .nfeArea .area-name {
        font-family: "Times New Roman", serif;
        color: #000;
        font-weight: bold;
        margin: 5px 0 0;
        font-size: 6pt;
        text-transform: uppercase;
    }

    .nfeArea .txt-upper {
        text-transform: uppercase;
    }

    .nfeArea .txt-center {
        text-align: center;
    }

    .nfeArea .txt-right {
        text-align: right;
    }

    .nfeArea .nf-label {
        text-transform: uppercase;
        margin-bottom: 3px;
        display: block;
    }

    .nfeArea .nf-label.label-small {
        letter-spacing: -0.5px;
        font-size: 4pt;
    }

    .nfeArea .info {
        font-weight: bold;
        font-size: 8pt;
        display: block;
        line-height: 1em;
    }

    .nfeArea table {
        font-family: "Times New Roman", serif;
        color: #000;
        font-size: 5pt;
        border-collapse: collapse;
        width: 100%;
        border-color: #000;
        border-radius: 5px;
    }

    .nfeArea .no-top {
        margin-top: -1px;
    }

    .nfeArea .mt-table {
        margin-top: 3px;
    }

    .nfeArea .valign-middle {
        vertical-align: middle;
    }

    .nfeArea td {
        vertical-align: top;
        box-sizing: border-box;
        overflow: hidden;
        border-color: #000;
        padding: 1px;
        height: 5mm;
    }

    .nfeArea .tserie {
        width: 32.2mm;
        vertical-align: middle;
        font-size: 8pt;
        font-weight: bold;
    }

    .nfeArea .tserie span {
        display: block;
    }

    .nfeArea .tserie h3 {
        display: inline-block;
    }

    .nfeArea .entradaSaida .legenda {
        text-align: left;
        margin-left: 2mm;
        display: block;
    }

    .nfeArea .entradaSaida .legenda span {
        display: block;
    }

    .nfeArea .entradaSaida .identificacao {
        float: right;
        margin-right: 2mm;
        border: 1px solid black;
        width: 5mm;
        height: 5mm;
        text-align: center;
        padding-top: 0;
        line-height: 5mm;
    }

    .nfeArea .hr-dashed {
        border: none;
        border-top: 1px dashed #444;
        margin: 5px 0;
    }

    .nfeArea .client_logo {
        height: 27.5mm;
        width: 28mm;
        margin: 0.5mm;
    }

    .nfeArea .title {
        font-size: 10pt;
        margin-bottom: 2mm;
    }

    .nfeArea .txtc {
        text-align: center;
    }

    .nfeArea .pd-0 {
        padding: 0;
    }

    .nfeArea .mb2 {
        margin-bottom: 2mm;
    }

    .nfeArea table table {
        margin: -1pt;
        width: 100.5%;
    }

    .nfeArea .wrapper-table {
        margin-bottom: 2pt;
    }

    .nfeArea .wrapper-table table {
        margin-bottom: 0;
    }

    .nfeArea .wrapper-table table+table {
        margin-top: -1px;
    }

    .nfeArea .boxImposto {
        table-layout: fixed;
    }

    .nfeArea .boxImposto td {
        width: 11.11%;
    }

    .nfeArea .boxImposto .nf-label {
        font-size: 5pt;
    }

    .nfeArea .boxImposto .info {
        text-align: right;
    }

    .nfeArea .wrapper-border {
        border: 1px solid #000;
        border-width: 0 1px 1px;
        height: auto;
    }

    .nfeArea .wrapper-border table {
        margin: 0 -1px;
        width: auto;
    }

    .nfeArea .content-spacer {
        display: block;
        height: 10px;
    }

    .nfeArea .titles th {
        padding: 3px 0;
    }

    .nfeArea .listProdutoServico td {
        padding: 0;
    }

    .nfeArea .codigo {
        display: block;
        text-align: center;
        margin-top: 5px;
    }

    .nfeArea .boxProdutoServico tr td:first-child {
        border-left: none;
    }

    .nfeArea .boxProdutoServico td {
        font-size: 6pt;
        height: auto;
    }

    .nfeArea .boxFatura span {
        display: block;
    }

    .nfeArea .boxFatura td {
        border: 1px solid #000;
    }

    .nfeArea .freteConta .border {
        width: 5mm;
        height: 5mm;
        float: right;
        text-align: center;
        line-height: 5mm;
        border: 1px solid black;
    }

    .nfeArea .freteConta .info {
        line-height: 5mm;
    }

    .page .boxFields td p {
        font-family: "Times New Roman", serif;
        font-size: 5pt;
        line-height: 1.2em;
        color: #000;
    }

    .nfeArea .imgCanceled {
        position: absolute;
        top: 75mm;
        left: 30mm;
        z-index: 3;
        opacity: 0.8;
        display: none;
    }

    .nfeArea.invoiceCanceled .imgCanceled {
        display: block;
    }

    .nfeArea .imgNull {
        position: absolute;
        top: 75mm;
        left: 20mm;
        z-index: 3;
        opacity: 0.8;
        display: none;
    }

    .nfeArea.invoiceNull .imgNull {
        display: block;
    }

    .nfeArea.invoiceCancelNull .imgCanceled {
        top: 100mm;
        left: 35mm;
        display: block;
    }

    .nfeArea.invoiceCancelNull .imgNull {
        top: 65mm;
        left: 15mm;
        display: block;
    }

    .nfeArea .page-break {
        page-break-before: always;
    }

    .nfeArea .block {
        display: block;
    }

    .label-mktup {
        font-family: Arial !important;
        font-size: 8px !important;
        padding-top: 8px !important;
    }
</style>
"""

input_string_html = F"""
<!DOCTYPE html>
<meta charset="utf-8"/>
<div class="page nfeArea">
    <div class="boxFields" style="padding-top: 20px;">
        <table cellpadding="0" cellspacing="0" border="1">
            <tbody>
                <tr>
                    <td colspan="2" class="txt-upper">
                        Recebemos de {x.emit.xNome} os produtos e serviços constantes na nota fiscal indicada
                        ao lado
                    </td>
                    <td rowspan="2" class="tserie txt-center">
                        <span class="font-12" style="margin-bottom: 5px;">NF-e</span>
                        <span>N° {x.ide.nNF}</span>
                        <span>Série {x.ide.serie}</span>
                    </td>
                </tr>
                <tr>
                    <td style="width: 32mm">
                        <span class="nf-label">Data de recebimento</span>
                    </td>
                    <td style="width: 124.6mm">
                        <span class="nf-label">Identificação de assinatura do Recebedor</span>
                    </td>
                </tr>
            </tbody>
        </table>
        <hr class="hr-dashed" />
        <table cellpadding="0" cellspacing="0" border="1">
            <tbody>
                <tr>
                    <td rowspan="3" style="width: 30mm">
                        <img class="client_logo" src="" alt=""
                            onerror=" javascript:this.src='data:image/png;base64," />
                    </td>
                    <td rowspan="3" style="width: 46mm; font-size: 7pt;" class="txt-center">
                        <span class="mb2 bold block">{x.emit.xNome}</span>
                        <span class="block">{x.emit.enderEmit.xLgr}</span>
                        <span class="block">
                            {x.emit.enderEmit.xBairro} - {x.emit.enderEmit.CEP}
                        </span>
                        <span class="block">
                            {x.emit.enderEmit.xMun} - {x.emit.enderEmit.UF} - Fone: {x.emit.enderEmit.fone}
                        </span>
                    </td>
                    <td rowspan="3" class="txtc txt-upper" style="width: 34mm; height: 29.5mm;">
                        <h3 class="title">Danfe</h3>
                        <p class="mb2">Documento auxiliar da Nota Fiscal Eletrônica </p>
                        <p class="entradaSaida mb2">
                            <span class="identificacao">
                                <span>{x.ide.tpNF}</span>
                            </span>
                            <span class="legenda">
                                <span>0 - Entrada</span>
                                <span>1 - Saída</span>
                            </span>
                        </p>
                        <p>
                            <span class="block bold">
                                <span>N°</span>
                                <span>{x.ide.nNF}</span>
                            </span>
                            <span class="block bold">
                                <span>SÉRIE:</span>
                                <span>{x.ide.serie}</span>
                            </span>
                            <span class="block">
                                <span>Página</span>
                                <span>[actual_page]</span>
                                <span>de</span>
                                <span>[total_pages]</span>
                            </span>
                        </p>
                    </td>
                    <td class="txt-upper" style="width: 80mm;">
                        <span class="nf-label">Controle do Fisco</span>
                        <img alt="" style=" font-size= 200%;width: 70mm;" src="data:image/svg+xml;base64, {encoded_string}"/>
                    </td>
                </tr>
                <tr>
                    <td>
                        <span class="nf-label">CHAVE DE ACESSO</span>
                        <span class="bold block txt-center info">{x.Id.replace("NFe","")}</span>
                    </td>
                </tr>
                <tr>
                    <td class="txt-center valign-middle">
                        <span class="block">Consulta de autenticidade no portal nacional da NF-e </span>
                        www.nfe.fazenda.gov.br/portal ou no site da Sefaz Autorizada.
                    </td>
                </tr>
            </tbody>
        </table>
        <!-- Natureza da Opera��o -->
        <table cellpadding="0" cellspacing="0" class="boxNaturezaOperacao no-top" border="1">
            <tbody>
                <tr>
                    <td>
                        <span class="nf-label">NATUREZA DA OPERAÇÃO</span>
                        <span class="info">{x.ide.natOp}</span>
                    </td>
                    <td style="width: 84.7mm;">
                        <span class="nf-label">PROTOCOLO</span>
                        <span class="info"></span>
                    </td>
                </tr>
            </tbody>
        </table>

        <!-- Inscri��o -->
        <table cellpadding="0" cellspacing="0" class="boxInscricao no-top" border="1">
            <tbody>
                <tr>
                    <td>
                        <span class="nf-label">INSCRIÇÃO ESTADUAL</span>
                        <span class="info">{x.emit.IE}</span>
                    </td>
                    <td style="width: 67.5mm;">
                        <span class="nf-label">INSCRIÇÃO ESTADUAL DO SUBST. TRIB.</span>
                        <span class="info"></span>
                    </td>
                    <td style="width: 64.3mm">
                        <span class="nf-label">CNPJ</span>
                        <span class="info">{x.emit.CNPJ}</span>
                    </td>
                </tr>
            </tbody>
        </table>

        <!-- Destinat�rio/Emitente -->
        <p class="area-name">Destinatário/Emitente</p>
        <table cellpadding="0" cellspacing="0" class="boxDestinatario" border="1">
            <tbody>
                <tr>
                    <td class="pd-0">
                        <table cellpadding="0" cellspacing="0" border="1">
                            <tbody>
                                <tr>
                                    <td>
                                        <span class="nf-label">NOME/RAZÃO SOCIAL</span>
                                        <span class="info">{x.dest.xNome}</span>
                                    </td>
                                    <td style="width: 40mm">
                                        <span class="nf-label">CNPJ/CPF</span>
                                        <span class="info">{x.dest.CNPJ}</span>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </td>
                    <td style="width: 22mm">
                        <span class="nf-label">DATA DE EMISSÃO</span>
                        <span class="info">{x.ide.dhEmi}</span>
                    </td>
                </tr>
                <tr>
                    <td class="pd-0">
                        <table cellpadding="0" cellspacing="0" border="1">
                            <tbody>
                                <tr>
                                    <td>
                                        <span class="nf-label">ENDEREÇO</span>
                                        <span class="info">{x.dest.enderDest.xLgr}</span>
                                    </td>
                                    <td style="width: 47mm;">
                                        <span class="nf-label">BAIRRO/DISTRITO</span>
                                        <span class="info">{x.dest.enderDest.xBairro}</span>
                                    </td>
                                    <td style="width: 37.2 mm">
                                        <span class="nf-label">CEP</span>
                                        <span class="info">{x.dest.enderDest.CEP}</span>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </td>
                    <td>
                        <span class="nf-label">DATA DE ENTR./SAÍDA</span>
                        <span class="info">{x.ide.dhSaiEnt}</span>
                    </td>
                </tr>
                <tr>
                    <td class="pd-0">
                        <table cellpadding="0" cellspacing="0" style="margin-bottom: -1px;" border="1">
                            <tbody>
                                <tr>
                                    <td>
                                        <span class="nf-label">MUNICÍPIO</span>
                                        <span class="info">{x.dest.enderDest.xMun}</span>
                                    </td>
                                    <td style="width: 34mm">
                                        <span class="nf-label">FONE/FAX</span>
                                        <span class="info">{x.dest.enderDest.fone}</span>
                                    </td>
                                    <td style="width: 28mm">
                                        <span class="nf-label">UF</span>
                                        <span class="info">{x.dest.enderDest.UF}</span>
                                    </td>
                                    <td style="width: 51mm">
                                        <span class="nf-label">INSCRIÇÃO ESTADUAL</span>
                                        <span class="info">{x.dest.IE}</span>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </td>
                    <td>
                        <span class="nf-label">HORA ENTR./SAÍDA</span>
                        <span id="info">{x.ide.dhSaiEnt}</span>
                    </td>
                </tr>
            </tbody>
        </table>
        <!-- Calculo do Imposto -->
        <p class="area-name">Calculo do imposto</p>
        <div class="wrapper-table">
            <table cellpadding="0" cellspacing="0" border="1" class="boxImposto">
                <tbody>
                    <tr>
                        <td>
                            <span class="nf-label label-small">BASE DE CÁLC. DO ICMS</span>
                            <span class="info">{x.total.ICMSTot.vBC}</span>
                        </td>
                        <td>
                            <span class="nf-label">VALOR DO ICMS</span>
                            <span class="info">{x.total.ICMSTot.vICMS}</span>
                        </td>
                        <td>
                            <span class="nf-label label-small" style="font-size: 4pt;">BASE DE CÁLC. DO ICMS ST</span>
                            <span class="info">{x.total.ICMSTot.vBCST}</span>
                        </td>
                        <td>
                            <span class="nf-label">VALOR DO ICMS ST</span>
                            <span class="info">{x.total.ICMSTot.vST}</span>
                        </td>
                        <td>
                            <span class="nf-label label-small">V. IMP. IMPORTAÇÃO</span>
                            <span class="info"></span>
                        </td>
                        <td>
                            <span class="nf-label label-small">V. ICMS UF REMET.</span>
                            <span class="info"></span>
                        </td>
                        <td>
                            <span class="nf-label">VALOR DO FCP</span>
                            <span class="info">{x.total.ICMSTot.vFCP}</span>
                        </td>
                        <td>
                            <span class="nf-label">VALOR DO PIS</span>
                            <span class="info">{x.total.ICMSTot.vPIS}</span>
                        </td>
                        <td>
                            <span class="nf-label label-small">V. TOTAL DE PRODUTOS</span>
                            <span class="info">{x.total.ICMSTot.vProd}</span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <span class="nf-label">VALOR DO FRETE</span>
                            <span class="info">{x.total.ICMSTot.vFrete}</span>
                        </td>
                        <td>
                            <span class="nf-label">VALOR DO SEGURO</span>
                            <span class="info">{x.total.ICMSTot.vSeg}</span>
                        </td>
                        <td>
                            <span class="nf-label">DESCONTO</span>
                            <span class="info">{x.total.ICMSTot.vDesc}</span>
                        </td>
                        <td>
                            <span class="nf-label">OUTRAS DESP.</span>
                            <span class="info">{x.total.ICMSTot.vOutro}</span>
                        </td>
                        <td>
                            <span class="nf-label">VALOR DO IPI</span>
                            <span class="info">{x.total.ICMSTot.vIPI}</span>
                        </td>
                        <td>
                            <span class="nf-label">V. ICMS UF DEST.</span>
                            <span class="info"></span>
                        </td>
                        <td>
                            <span class="nf-label label-small">V. APROX. DO TRIBUTO</span>
                            <span class="info"></span>
                        </td>
                        <td>
                            <span class="nf-label label-small">VALOR DA CONFINS</span>
                            <span class="info">{x.total.ICMSTot.vCOFINS}</span>
                        </td>
                        <td>
                            <span class="nf-label label-small">V. TOTAL DA NOTA</span>
                            <span class="info">{x.total.ICMSTot.vNF}</span>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
        <!-- Transportador/Volumes transportados -->
        <p class="area-name">Transportador/volumes transportados</p>
        <table cellpadding="0" cellspacing="0" border="1">
            <tbody>
                <tr>
                    <td>
                        <span class="nf-label">RAZÃO SOCIAL</span>
                        <span class="info"></span>
                    </td>
                    <td class="freteConta" style="width: 32mm">
                        <span class="nf-label">FRETE POR CONTA</span>
                        <div class="border">
                            <span class="info">{x.transp.modFrete}</span>
                        </div>
                        <p>0 - Emitente</p>
                        <p>1 - Destinatário</p>
                    </td>
                    <td style="width: 17.3mm">
                        <span class="nf-label">CÓDIGO ANTT</span>
                        <span class="info"></span>
                    </td>
                    <td style="width: 24.5mm">
                        <span class="nf-label">PLACA</span>
                        <span class="info"></span>
                    </td>
                    <td style="width: 11.3mm">
                        <span class="nf-label">UF</span>
                        <span class="info"></span>
                    </td>
                    <td style="width: 29.5mm">
                        <span class="nf-label">CNPJ/CPF</span>
                        <span class="info"></span>
                    </td>
                </tr>
            </tbody>
        </table>

        <table cellpadding="0" cellspacing="0" border="1" class="no-top">
            <tbody>
                <tr>
                    <td class="field endereco">
                        <span class="nf-label">ENDEREÇO</span>
                        <span class="content-spacer info"></span>
                    </td>
                    <td style="width: 32mm">
                        <span class="nf-label">MUNICÍPIO</span>
                        <span class="info"></span>
                    </td>
                    <td style="width: 31mm">
                        <span class="nf-label">UF</span>
                        <span class="info"></span>
                    </td>
                    <td style="width: 51.4mm">
                        <span class="nf-label">INSC. ESTADUAL</span>
                        <span class="info"></span>
                    </td>
                </tr>
            </tbody>
        </table>
        <table cellpadding="0" cellspacing="0" border="1" class="no-top">
            <tbody>
                <tr>
                    <td class="field quantidade">
                        <span class="nf-label">QUANTIDADE</span>
                        <span class="content-spacer info"></span>
                    </td>
                    <td style="width: 31.4mm">
                        <span class="nf-label">ESPÉCIE</span>
                        <span class="info">[ds_transport_type_volumes_transported]</span>
                    </td>
                    <td style="width: 31mm">
                        <span class="nf-label">MARCA</span>
                        <span class="info"></span>
                    </td>
                    <td style="width: 31.5mm">
                        <span class="nf-label">NUMERAÇÃO</span>
                        <span class="info">[ds_transport_number_volumes_transported]</span>
                    </td>
                    <td style="width: 31.5mm">
                        <span class="nf-label">PESO BRUTO</span>
                        <span class="info"></span>
                    </td>
                    <td style="width: 32.5mm">
                        <span class="nf-label">PESO LÍQUIDO</span>
                        <span class="info"></span>
                    </td>
                </tr>
            </tbody>
        </table>
        <!-- Dados do produto/servi�o -->
        <p class="area-name">Dados do produto/serviço</p>
        <div class="wrapper-border">
            <table cellpadding="0" cellspacing="0" border="1" class="boxProdutoServico" id="grid">
                <thead class="listProdutoServico" id="table">
                    <tr class="titles">
                        <th class="cod" style="width: 15.5mm">CÓDIGO</th>
                        <th class="descrit" style="width: 66.1mm">DESCRIÇÃO DO PRODUTO/SERVIÇO</th>
                        <th class="ncmsh">NCMSH</th>
                        <th class="cst">CST</th>
                        <th class="cfop">CFOP</th>
                        <th class="un">UN</th>
                        <th class="amount">QTD.</th>
                        <th class="valUnit">VLR.UNIT</th>
                        <th class="valTotal">VLR.TOTAL</th>
                        <th class="bcIcms">BC ICMS</th>
                        <th class="valIcms">VLR.ICMS</th>
                        <th class="valIpi">VLR.IPI</th>
                        <th class="aliqIcms">ALIQ.ICMS</th>
                        <th class="aliqIpi">ALIQ.IPI</th>
                    </tr>
                </thead>
                <tbody>
                    {texto}
            </table>
        </div>

        <!-- Dados adicionais -->
        <p class="area-name">Dados adicionais</p>
        <table cellpadding="0" cellspacing="0" border="1" class="boxDadosAdicionais">
            <tbody>
                <tr>
                    <td class="field infoComplementar">
                        <span class="nf-label">INFORMAÇÕES COMPLEMENTARES</span>
                        <span>{x.infAdic.infCpl}</span>
                    </td>
                    <td class="field reservaFisco" style="width: 85mm; height: 24mm">
                        <span class="nf-label">RESERVA AO FISCO</span>
                        <span></span>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</div>
"""

str_pronta = input_string_css + input_string_html
# print(str_pronta)

options = {
    'quiet': ''
}

id = x.Id.replace("NFe", "")
config = pdfkit.configuration(
    wkhtmltopdf="C:\\Program Files (x86)\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
pdfkit.from_string(str_pronta, F"{id}.pdf",
                   configuration=config, options=options)

image_file.close()

file2 = id + ".svg"
os.remove(file2)
