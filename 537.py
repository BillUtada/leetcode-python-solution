class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        an = int(a[0:str(a).find("+")]);
        ai = int(a[str(a).find("+")+1:str(a).find("i")]);
        bn = int(b[0:str(b).find("+")]);
        bi = int(b[str(b).find("+")+1:str(b).find("i")]);
        
        n = an * bn - ai * bi;
        i = an * bi + ai * bn;
        res = str(n) + "+" + str(i) + "i";
        return res;
            
