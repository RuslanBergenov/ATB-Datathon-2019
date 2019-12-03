select distinct	GEO,
                        REPLACE(CONCAT(Indicator,'_',IndicatorLevel,'_',[Unit of Measure]), ' ', '') as Parameter, sum (Value) as SumValue
                       from [dbo].[censusmat] where SourceTable in 
                       (32100426, 32100432, 32100446 )
                       group by GEO,  REPLACE(CONCAT(Indicator,'_',IndicatorLevel,'_',[Unit of Measure]), ' ', '')



select distinct [unit of measure] from [dbo].[censusmat] where Indicator = 'Bees'







-- Nrow by Source Table
select SourceTable, count (SourceTable) as Nrow
from [dbo].[v_Census]
group by SourceTable
order by SourceTable



-- total nrow
select count (SourceTable) as Nrow
from  [dbo].[v_Census]


--- select 
select top 100 * from [dbo].[v_Census]
select distinct geo from [dbo].[v_Census]


--- select 
select top 100 * from [dbo].[CensusMat]
select distinct geo from [dbo].[CensusMat]


select 'census'
	select count (SourceTable) from [dbo].[census]
	select top 100 * from [dbo].[census]

select 'CensusMat'
	select count (SourceTable) from [dbo].[censusmat]
	select top 100 * from [dbo].[censusmat]

select 'dataset'
	select * from [dbo].[dataset]

select 'GEO'
	select   * from [dbo].[GEO]




select distinct Indicator, IndicatorLevel, [Unit of measure] from [dbo].[CensusMat]
order by Indicator, IndicatorLevel, [Unit of measure]




select * from [dbo].[censusmat] where SourceTable = 32100446

select distinct REF_DATE,GEO
Indicator,IndicatorLevel,[Unit of Measure], sum (Value) as SumValue
 from [dbo].[censusmat] where SourceTable = 32100446 
 group by REF_DATE,GEO,
Indicator,IndicatorLevel,[Unit of Measure]


