1.提示：name全空白时raise SystemExit(2)，禁止使用p.error，用pytest校验
2.初始状态：新增测试用例后test_main_blank_name失败，不会抛出SystemExit
3.智能体改动：参数解析完成后增加空白校验，raise SystemExit(2)
4.人工diff检查：无无关修改，pytest两个用例全部通过。
