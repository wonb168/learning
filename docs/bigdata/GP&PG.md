# 自定义函数
1. 周一函数

```
CREATE OR REPLACE FUNCTION public.get_monday(dt timestamp)
 RETURNS timestamp
 LANGUAGE plpgsql
AS $function$
begin --select get_monday('2021-04-04'::timestamp)
	return dt-(mod((EXTRACT(DOW FROM dt)+6)::int,7)||' days')::interval;
END
$function$
;
```

