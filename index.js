function CarregarLista(lista) {
    $('#grid > tbody').empty();

    for (var i = 0; i < 44; i++) {
        var html = '<tr>' +
            '<td>' + lista[i].cProd + '</td>' +
            '<td>' + lista[i].xProd + '</td>' +
            '<td>' + lista[i].NCMSH + '</td>' +
            '<td>' + lista[i].CST + '</td>' +
            '<td>' + lista[i].CFOP + '</td>' +
            '<td>' + lista[i].uCom + '</td>' +
            '<td>' + lista[i].qCom + '</td>' +
            '<td>' + lista[i].vUnCom+ '</td>' +
            '<td>' + lista[i].vProd + '</td>' +
            '</tr>'
        $('#grid > tbody').append(html);
    }
}