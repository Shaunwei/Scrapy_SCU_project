

link = sel.xpath("//tr//a/@href").extract()
for l in link:
    l = "'" + l + "'" + ","
    %save -r -a temp l
