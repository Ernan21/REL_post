SELECT o.nome AS "nome", SUM(vi.valortotal) AS "quantidade"
FROM 
    pdv.vendaitem vi
    INNER JOIN pdv.venda v ON v.id = id_venda
    INNER JOIN pdv.operador o ON o.matricula = v.matricula
WHERE vi.data = CURRENT_DATE
    AND v.cancelado = FALSE
    AND vi.cancelado = FALSE
GROUP BY o.nome
ORDER BY SUM(vi.valortotal) DESC, COUNT(*) ASC